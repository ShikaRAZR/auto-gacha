import random
import os
import sys

# Get the path to the folder containing your scripts
# This assumes myLib.sikuli and GFL1Dailies.sikuli are in the same parent folder
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: 
    sys.path.append(myPath)

# Now you can import your library
from myLib import *

# Project Neural Cloud - 1080p, windows 11, mumuplayer, pnc snap on bottom right