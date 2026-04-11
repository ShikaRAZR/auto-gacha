import random
import os
import sys

# Get the path to the folder containing your scripts
# This assumes myLib.sikuli and Test.sikuli are in the same parent folder
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: 
    sys.path.append(myPath)

# Now you can import your library
from myLib import *

click_random_img("test2.png")