"""
Waydroid ORB Image Recognition Library

Function helpers for automation, using OpenCV (ORB) + ADB to detect, find, and tap images
Documentation:
https://developer.android.com/tools/adb


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
    # Supposedly the CORRECT WAY, exec-out gets raw binary output back to python, BUT FAILS:
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

# screenshot(os.path.expanduser("~/Downloads/screen.png"))
tap(300,300)
swipe(300,400,600,500,1000)