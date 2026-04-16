"""
Waydroid ORB Image Recognition Library

Function helpers for automation, using OpenCV (ORB) + ADB to detect, find, and tap images
Documentation:
https://developer.android.com/tools/adb
https://github.com/ImranNawar/orb_feature_descriptor
https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html?
https://www.geeksforgeeks.org/python/opencv-python-tutorial/

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
    uv run --with opencv-python --with numpy myLib.py
"""

import cv2
import numpy as np
import subprocess
import os, sys
import random
import math
import time

# Config
WAYDROID_IP   = "192.168.240.112:5555"   # Waydroid IP
# Debug Directory
'''
DEBUG_DIR  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Debug")
DEBUG_PATH = os.path.join(DEBUG_DIR, "screen_debug.png")
os.makedirs(DEBUG_DIR, exist_ok=True) # Makes Directory if it doesnt exist
'''
DEBUG_PATH = None
# Image Directory
MAIN_DIR  = os.path.dirname(os.path.abspath(__file__))
IMG_DIR: str = None
counter: int = 0


# Global Var Helpers
def set_game_img_folder(folder: str):
    global IMG_DIR
    global MAIN_DIR
    IMG_DIR = os.path.join(MAIN_DIR, folder)

# Helpers
def wait(rand_start: float = None, rand_end: float = None): 
    # waits for a certain time (seconds float var type), 1 paramter waits for static time, 2 parameters waits for a random time in between
    if rand_start>2:
        print("------------------------------------------------long sleep start")
    if rand_end is None:
        time.sleep(rand_start)
    else:
        time.sleep(random.uniform(rand_start, rand_end))

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
    print(f"Dragged for {duration_ms}ms ({x1}, {y1}), ({x2}, {y2})")

def scroll(x: int, y: int, distance_px: int = 30, repeat: int = 1, duration_ms: int = 300, direction: str = "up"): # "up" or "down"
    if direction != "down" and direction != "up":
        print("Invalid Scroll")
        return
    if direction == "down":
        distance_px = distance_px * -1
    for i in range(repeat):
        adb("shell", "input", "swipe",
        str(x), str(y), str(x), str(y+distance_px), str(int(duration_ms/repeat)))
        wait(0.3)

# OpenCV
def find_template( # finds a template on waydroid screen
    template_path: str, # path to template png
    similarity: float = 0.8, # match confidence  0.0-1.0
    screen: np.ndarray = None, # optional precaptured screen
    region:  tuple[int, int, int, int] | None = None, # (x1, y1, x2, y2) top left, bottom right corners, can be a tuple or None, set to None as default
    debug_path: str = None # sends debug PNG with rectangle drawn
) -> tuple[int, int, int, int] | None: # returns (center_x, center_y) of the best match, or None if below threshold.
    # Load template (screenshot) in grayscale format
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise FileNotFoundError(f"Template not found: {template_path}")
    # Reads the dimensions of the template (help with returning coordinates)
    t_h, t_w = template.shape[:2]
    # Grab screen if not provided
    if screen is None:
        screen = screenshot()
    
    if region is not None:
        x1, y1, x2, y2 = region
        print(f"filtered region: {x1}, {y1}, {x2}, {y2}")
        screen = screen[y1:y2, x1:x2]  # numpy slicing is [rows, cols] = [y, x]
    # converts BGR format to grayscale
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # template is compared to screen using cv2.TM_CCOEFF_NORMED technique, 1.0 = perfect match, 0.0 = no match
    # result - 2D grid of scores, one score for each pixel
    # Example: 
    # screen is 1280x720, template is 80x100, result map is (1280-80) x (720-100) = 1200x620 - one score per position
    # template is slided across every possible postition on screen, smaller template = more positions it can be slided onto
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    # minMaxLoc scans result map and returns:
    # min_val - lowest score in result map
    # max_val - highest score in result map
    # min_loc - location of lowest score (top left of matched region)
    # max_loc - location of highest score (top left of matched region)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # [match or no match] and [best score and location]
    if max_val >= similarity:
        print(f"Template found, score: {max_val:.3f} | {max_loc} {(max_loc[0] + t_w), (max_loc[1] + t_h)} | {os.path.basename(template_path)}")
    if max_val < similarity:
        print(f"No match, (score {max_val:.3f} < {similarity}) | {os.path.basename(template_path)}")
        return None

    # top left, bottom right corners template
    x1 = max_loc[0]
    y1 = max_loc[1]
    x2 = max_loc[0] + t_w
    y2 = max_loc[1] + t_h

    if debug_path:
        # add half the template size to get the CENTER for tapping
        cx = max_loc[0] + t_w // 2
        cy = max_loc[1] + t_h // 2
        # draw on debug_screen
        debug_screen = screen.copy() # copies grayscale screen
        top_left = max_loc # top left of best match
        bottom_right = (top_left[0] + t_w, top_left[1] + t_h) # bottom right of best match
        cv2.rectangle(debug_screen, top_left, bottom_right, 0, 2) # draws rectangle on debug_screen, with coord, black color (0) thickness (2) 
        # cv2.circle(debug_screen, (cx, cy), 6, 0, -1) # draws circle on center of match on debug screen, radius (6px), black color (0) thickness (-1 means fill circle)
        '''
        cv2.imshow("debug", debug_screen) # displays image on desktop
        cv2.waitKey(2000)   # windows stays open for 1 second
        cv2.destroyAllWindows()
        '''
        # Combine template, debug_screen
        pad_height = screen.shape[0] - template.shape[0] # (pad - template) height, to add the difference to template
        pad = np.full((pad_height, template.shape[1]), 0, dtype=np.uint8)  # black padding
        padded_template = np.vstack([template, pad]) # add padding under template, template/debug_screen are same height now
        combined = np.hstack([padded_template, debug_screen])# Combine template image and debug_screen
        # Saves image to debug_path
        cv2.imwrite(debug_path, combined)
        #print(f"Debug image saved to: {debug_path}")

    # returns coordinates of best match, top left corner, bottom right corner
    return x1, y1, x2, y2
    

def get_random_coordinates(x1, y1, x2, y2) -> tuple[int, int]:
    # Randomized cordinates between two points
    # Create a dynamic margin (10% of the image's width and height)
    margin_x = int((x2-x1) * 0.1)
    margin_y = int((y2-y1) * 0.1)
    # Add the margin to the minimums, and subtract it from the maximums
    rx = random.randint(x1 + margin_x, x2 - margin_x)
    ry = random.randint(y1 + margin_y, y2 - margin_y)
    return rx, ry


# High Level Actions
def exists_similar_img(
    image_name: str, 
    similarity: float = 0.8, 
    auto_wait_timeout: int = 2, # how many seconds it stays searching image
    debug_path: str = DEBUG_PATH
) -> tuple[int, int, int, int] | None: # returns top left and bottom right coordinates of image
    # loop searching template
    template_path = os.path.join(IMG_DIR, image_name)# combines path and image name
    template_coord = None
    # Looks for image every second for "auto_wait_timeout" times
    template_coord = find_template(template_path=template_path, similarity=similarity, debug_path=debug_path)
    for i in range(auto_wait_timeout-1):
        if template_coord is not None:
            break
        wait(1)
        template_coord = find_template(template_path=template_path, similarity=similarity, debug_path=debug_path)
    if template_coord is not None:
        return template_coord
    print(f"------------------------------------------------1failed to find image: {image_name}")
    return None

def click_random_img( # click_random_img
    image_name: str, 
    similarity: float = 0.8, 
    repeat: int = 1, # how many times to click on image
    rand_start: float = 0.0, # random start range between repeat clicks
    rand_end: float = 0.0, # random end range between repeat clicks
    auto_wait_timeout: int = 5, # how many seconds it stays searching image
    debug_path: str = DEBUG_PATH
) -> tuple[int, int] | None: # returns coordinates that were clicked

    template_coord = exists_similar_img(image_name=image_name, similarity=similarity, auto_wait_timeout=auto_wait_timeout, debug_path=debug_path)
    if repeat == 0:
        print("Repeat 0, Nothing Clicked")
        return None
    if template_coord is not None:
        for i in range(repeat):
            rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
            tap(rx,ry)
            wait(rand_start, rand_end)
        wait(1.0, 2.0) # wait for screen to load before next detection
        return rx, ry
    print(f"------------------------------------------------2failed to tap image: {image_name}")
    return None

def drag_random_img_to_dst( # Drag Img1 to Img2 on random section of each image
    img1: str, 
    img2: str, 
    similarity: float = 0.8,
    auto_wait_timeout: int = 2,
    debug_path: str = DEBUG_PATH
) -> tuple[int, int, int, int] | None: # returns coordinates that were clicked for both images

    template_coord1 = exists_similar_img(img1, similarity=similarity, auto_wait_timeout=auto_wait_timeout, debug_path=debug_path)
    template_coord2 = exists_similar_img(img2, similarity=similarity, auto_wait_timeout=auto_wait_timeout, debug_path=debug_path)

    if template_coord1 and template_coord2:
        rx1, ry1 = get_random_coordinates(template_coord1[0], template_coord1[1], template_coord1[2], template_coord1[3])
        rx2, ry2 = get_random_coordinates(template_coord2[0], template_coord2[1], template_coord2[2], template_coord2[3])
        distance = int(math.sqrt((rx2 - rx1)**2 + (ry2 - ry1)**2)) # Pythagorean theorem distance between two points
        swipe(rx1, ry1, rx2, ry2, duration_ms = distance*2)
        wait(1.0, 2.0)
        return rx1, ry1, rx2, ry2
    print(f"------------------------------------------------3failed to swipe images: {img1}, {img2}")
    return None

def exist_similar_img_searcharea_below( # see if img below anchor_img exists
    anchor_img: str, # anchor Image
    img: str, # image that is searched below anchor image
    px: int = None, # how many pixels down you search
    anchor_similarity=0.8, 
    img_similarity=0.8,
    auto_wait_timeout=2,
    debug_path: str = DEBUG_PATH
) -> tuple[int, int, int, int] | None:

    if px is None:
        print(f"------------------------------------------------invalid region")
        return None
    anchor_coord = exists_similar_img(anchor_img, similarity=anchor_similarity, auto_wait_timeout=auto_wait_timeout, debug_path=debug_path)
    if anchor_coord:
        x1, y1, x2, y2 = anchor_coord
        # Search Area Below
        region_x1 = x1
        region_y1 = y2
        region_x2 = x2
        region_y2 = y2 + px
        region = region_x1, region_y1, region_x2, region_y2
        # loop searching template
        template_path = os.path.join(IMG_DIR, img)# combines path and image name
        template_coord = None
        # Looks for image every second for "auto_wait_timeout" times
        template_coord = find_template(template_path=template_path, similarity=img_similarity, region=region, debug_path=debug_path)
        for i in range(auto_wait_timeout-1):
            if template_coord is not None:
                break
            wait(1)
            template_coord = find_template(template_path=template_path, similarity=img_similarity, region=region, debug_path=debug_path)
        if template_coord is not None:
            temp_x1, temp_y1, temp_x2, temp_y2 = template_coord
            return (
                temp_x1 + region_x1,
                temp_y1 + region_y1,
                temp_x2 + region_x1,
                temp_y2 + region_y1
            )
        print(f"------------------------------------------------4failed to find image: {img}")
        return None
    return None

def click_random_img_searcharea_below( # if img below anchor_img exists, click
    anchor_img: str, # anchor Image
    img: str, # image that is searched below anchor image
    px: int = None, # how many pixels down you search
    anchor_similarity=0.8, 
    img_similarity=0.8,
    auto_wait_timeout=2,
    debug_path: str = DEBUG_PATH
) -> tuple[int, int, int, int] | None:

    if px is None:
        print(f"------------------------------------------------invalid region")
        return None
    # check if img in search area exists and return coordinates
    template_coord = exist_similar_img_searcharea_below(
        anchor_img=anchor_img, 
        img=img, 
        px=px, 
        anchor_similarity=anchor_similarity, 
        img_similarity=img_similarity, 
        auto_wait_timeout=auto_wait_timeout, 
        debug_path=debug_path)
    # tap on random coordinates
    if template_coord is not None:
        rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
        tap(rx,ry)
        wait(1.0, 2.0)
        return rx,ry
    print(f"------------------------------------------------6failed to tap search area image: {img}")
    return None


def run():
    #exists_similar_img("select-equip.png")
    #click_random_img("select-equip.png")
    #drag_random_img_to_dst("select-equip.png", "component-enhancement.png")
    '''
    click_random_img_searcharea_below("petri-dish.png","coalition-drill-attack.png", 300, anchor_similarity=0.99)
    wait(2)
    click_random_img_searcharea_below("training-keycode.png","coalition-drill-attack.png", 300, anchor_similarity=0.99)
    wait(2)
    click_random_img_searcharea_below("rapid-growth-disk.png","coalition-drill-attack.png", 300, anchor_similarity=0.99)
    
    template_coord=exists_similar_img("combat-chapter-ep.png")
    rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
    scroll(rx,ry, distance_px= 200, repeat = 4, duration_ms = 300, direction = "up")
    '''
    print("test")


# screenshot(os.path.expanduser("~/Downloads/screen.png"))
# tap(300,300)
# swipe(300,400,600,500,1000)
#template_path = os.path.expanduser("~/Downloads/Waydroid_Test/GFLImages/select-equip.png")
#template_path = os.path.expanduser("~/Downloads/Waydroid_Debug/GFLImages/component-enhancement.png")
#find_template(template_path=template_path, debug_path=debug_path)





































'''
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

def find_template_orb(
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
    cx = int(np.mean(screen_pts[:, 0]))
    cy = int(np.mean(screen_pts[:, 1]))
    
    
    # top-left corner
    cx1 = int(np.min(screen_pts[:, 0]))
    cy1 = int(np.min(screen_pts[:, 1]))
    
    # top-right corner
    cx = int(np.max(screen_pts[:, 0]))
    cy = int(np.min(screen_pts[:, 1]))

    # bottom-left corner
    cx = int(np.min(screen_pts[:, 0]))
    cy = int(np.max(screen_pts[:, 1]))
    
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
    print(find_template_orb(screen, template, orb))
'''