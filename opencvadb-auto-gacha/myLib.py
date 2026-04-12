"""
Waydroid ORB Image Recognition Library

Function helpers for automation, using OpenCV (ORB) + ADB to detect, find, and tap images
Documentation:
https://developer.android.com/tools/adb
https://github.com/ImranNawar/orb_feature_descriptor
https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html?


Requirements:
sudo pacman -S android-tools python uv

Usage:
    waydroid prop set persist.waydroid.adb true
    waydroid session stop
    waydroid show-full-ui
# survives restarts

    adb connect 192.168.240.112:5555 
# Inside Waydroid, go to Settings → About phone → IP address to find the container IP
# Need to do every restart

    adb devices
    waydroid status
# shows device, test if active


Run:
    uv run --with opencv-python-headless --with numpy myLib.py




"""

import cv2
import numpy as np
import subprocess
import os


# Config
WAYDROID_IP   = "192.168.240.112:5555"   # Waydroid IP
# MIN_MATCHES   = 12     # minimum good keypoint matches to consider it found
# DISTANCE_CAP  = 55     # lower = stricter match (0–100 range for ORB)


# ADB Helpers
def adb(*args): # used for screenshotting, tapping, swipping a specific adb device
    """Run an adb command targeting WAYDROID_IP."""
    return subprocess.run(
        ["adb", "-s", WAYDROID_IP, *args],
        capture_output=True # hides command from displaying in terminal
    )


def screenshot(path: str = None) -> np.ndarray:
    # Example subprocess terminal command (adb, connect to waydroid, shell session, screenshot, -p (specify PNG format)):
    # adb -s 192.168.240.112:5555 shell screencap -p > ~/Downloads/screentest.png
    # Supposedly the CORRECT WAY, 'exec-out' gets raw binary output back to python, BUT FAILS:
    # adb -s 192.168.240.112:5555 exec-out screencap -p > ~/Downloads/screentest.png
    """Capture Waydroid screen via ADB, return as BGR numpy array."""
    result = adb("shell", "screencap", "-p")
    if not result.stdout: # if result is none
        raise RuntimeError("screencap returned nothing — is Waydroid running?")
    arr = np.frombuffer(result.stdout, dtype=np.uint8) # Converts raw PNG bytes from ADB to numpy array, unsigned 8-bit integers 
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR) # Decodes flat numpy array into BGR image OpenCV can use
    if img is None:
        raise RuntimeError("Failed to decode screenshot PNG")
    if path: # if there is a path, that is where image will be saved
        with open(path, "wb") as f: # opens file at path writing in binary mode (wb), meant to write images/media/exe/zip, any binary files
            print("Printing img to: "+path)
            f.write(result.stdout) # writes PNG bytes
    return img


def tap(x: int, y: int):
    # Example subprocess terminal command (adb, connect to waydroid, with a shell session, input tap at coordinates):
    # adb -s 192.168.240.112:5555 shell input tap 540 960
    """Send a tap event to Waydroid at (x, y)."""
    adb("shell", "input", "tap", str(x), str(y))
    print(f"Tapped ({x}, {y})")

def swipe(x1: int, y1: int, x2: int, y2: int, duration_ms: int = 300):
    """Send a swipe event."""
    adb("shell", "input", "swipe",
        str(x1), str(y1), str(x2), str(y2), str(duration_ms))



# ORB Matching
def build_orb():
    # Create an ORB detector
    # nfeatures=1000 tuned for small UI elements
    # nfeatures are keypoints ORB will look for, the more keypoints the more patterns it can match but requires more processing
    return cv2.ORB_create(nfeatures=500)

def extract_features(orb, img_bgr: np.ndarray):
    # Convert to grayscale
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    # compute ORB keypoints + descriptors
    keypoints, descriptors = orb.detectAndCompute(gray, None) # None (passes the entire screen) is where you pass a mask, to restrict region of detection
    return keypoints, descriptors

def find_template(
    screen_bgr: np.ndarray, # waydroid screen
    template_bgr: np.ndarray, # screenshot you are searching
    orb,
    min_matches: int = 8, # minimum good keypoint matches to consider it found, filter quantity - how similar each match is (affected by template resolution and size, less pixels is less keypoints)
    distance_cap: int = 65, # lower = stricter match (0–100 range for ORB), filter quality - how many good matches there are (affected by blur, compression, color, slight rendering changes, dpi)
) -> tuple[int, int] | None: # function returns coordinates, none if not found
    
    # Debug Testing Only
    save_debug_image(
        screen_bgr=screen_bgr, 
        template_bgr=template_bgr, 
        orb=orb, 
        center=None, 
        min_matches=min_matches, 
        distance_cap=distance_cap)

    # save keypoints and descriptors for template_bgr and screen_bgr using ORB feature matching.
    kp_template, des_template, = extract_features(orb, template_bgr) # python lets you save 2 values into 2 var on one line
    kp_screen, des_screen = extract_features(orb, screen_bgr)
    
    # Returns None if no descriptors found, image may have too little features (maybe a black screen)
    if des_template is None or des_screen is None:
        print("  No descriptors found — template or screen may be featureless")
        return None

    # Brute-force Hamming matcher (BFMatcher+NORM_HAMMING), ORB is best used with this technique and measurement, it is a stack designed for each other to be very compute efficient
    # cv2.BFMatcher - technique used to compare descriptors, cv2.NORM_HAMMING - measurement using bit differences, crossCheck=True - template and screen have to be best matches for EACH OTHER
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) 
    # compares every descriptor in template to every descriptor in screen 
    # and returns single best match for each template descriptor (List of DMatch Objects)
    matches = matcher.match(des_template, des_screen)

    # Keep only close matches
    # first m is saved into good, a list
    # for m in matches - interate through DMatch List
    # if distance_cap is lower the more strict the matches are, it is the cutoff for close matching
    good = [m for m in matches if m.distance < distance_cap]
    # sorts the list from lowest to highest (best match is first)
    good = sorted(good, key=lambda m: m.distance)

    print(f"  ORB matches: {len(good)} good / {len(matches)} total "
          f"(need {min_matches})")

    # there has to be enough good matches to confidently find a template on screen
    if len(good) < min_matches:
        return None

    
    # Compute the center of matched screen keypoints
    screen_pts = np.float32(
        [kp_screen[m.trainIdx].pt for m in good]
    )
    '''
    cx = int(np.mean(screen_pts[:, 0]))
    cy = int(np.mean(screen_pts[:, 1]))
    '''
    # top-left corner
    cx1 = int(np.min(screen_pts[:, 0]))
    cy1 = int(np.min(screen_pts[:, 1]))
    
    '''
    # top-right corner
    cx = int(np.max(screen_pts[:, 0]))
    cy = int(np.min(screen_pts[:, 1]))

    # bottom-left corner
    cx = int(np.min(screen_pts[:, 0]))
    cy = int(np.max(screen_pts[:, 1]))
    '''

    
    # bottom-right corner
    cx2 = int(np.max(screen_pts[:, 0]))
    cy2 = int(np.max(screen_pts[:, 1]))
    
    # Returns (center_x, center_y) if found
    return cx1, cy1, cx2, cy2
    # return cx, cy


def save_debug_image(
    screen_bgr: np.ndarray,
    template_bgr: np.ndarray,
    orb,
    center: tuple[int, int] | None,
    path=os.path.expanduser("~/Downloads/Waydroid_Test/screen_debug.png"),
    min_matches: int = 12, 
    distance_cap: int = 55,
):
    """Draw matches and save to disk for inspection."""
    kp_tmpl, des_tmpl = extract_features(orb, template_bgr)
    kp_screen, des_screen = extract_features(orb, screen_bgr)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(des_tmpl, des_screen)
    good = sorted(
        [m for m in matches if m.distance < distance_cap],
        key=lambda m: m.distance
    )[:30]  # draw at most 30 for clarity

    debug = cv2.drawMatches(
        template_bgr, kp_tmpl,
        screen_bgr, kp_screen,
        good, None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )
    if center:
        # Mark the detected center on the screen half
        offset_x = template_bgr.shape[1] + center[0]
        cv2.circle(debug, (offset_x, center[1]), 20, (0, 255, 0), 3)
        cv2.putText(debug, "FOUND", (offset_x - 30, center[1] - 28),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imwrite(path, debug)
    print(f"  Debug image saved → {path}")

def test():
    screen = screenshot()
    template = cv2.imread(os.path.expanduser("~/Downloads/Waydroid_Test/GFLImages/select-equip.png"))
    orb = build_orb()
    print(find_template(screen, template, orb))
    

test()
# screenshot(os.path.expanduser("~/Downloads/screen.png"))
# tap(300,300)
# swipe(300,400,600,500,1000)