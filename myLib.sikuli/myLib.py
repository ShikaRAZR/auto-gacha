from sikuli import *
import random
import math

# Default Similarity Score is 0.7 (70%)
# General
screen = 2
Settings.MoveMouseDelay = .1
Settings.AutoWaitTimeout = 5 # looks for images for 3 seconds
Settings.OcrTextRead = True
Settings.OcrTextSearch = True

def wait_random(start, end): # start, end arguments are int
    sleep_time = random.uniform(start,end)
    wait(sleep_time)

def click_random_img(img, similarity=0.8, repeat=1, rand_start=0.0, rand_end=0.0, auto_wait_timeout=5):
    Settings.AutoWaitTimeout = auto_wait_timeout
    scr = Screen(screen) # Set screen to search for img
    match = scr.exists(Pattern(img).similar(similarity)) # check if img exists on screen, can be 80% similar 
    if match:
        # Randomize area of clicking on the image
        # Create a dynamic margin (10% of the image's width and height)
        margin_x = int(match.w * 0.1)
        margin_y = int(match.h * 0.1)
        # Add the margin to the minimums, and subtract it from the maximums
        rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
        ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
        match.highlight(0.1) # Highlights area detected, also acts like a sleep function
        for i in range(repeat):
            wait(random.uniform(rand_start, rand_end))
            scr.click(Location(rx,ry))
        wait(random.uniform(0.5, 1.0)) # wait for screen to load before next detection
        return True
    print("failed to find: "+img)
    return False

def drag_random_img_to_dst(img1, img2, similarity=0.8): # Drag Img to Destination
    scr = Screen(screen)
    match1 = scr.exists(Pattern(img1).similar(similarity))
    match2 = scr.exists(Pattern(img2).similar(similarity))
    if match1 and match2:
        margin1_x = int(match1.w * 0.5)
        margin1_y = int(match1.h * 0.5)
        rx1 = random.randint(match1.x + margin1_x, match1.x + match1.w - margin1_x)
        ry1 = random.randint(match1.y + margin1_y, match1.y + match1.h - margin1_y)
        margin2_x = int(match2.w * 0.5)
        margin2_y = int(match2.h * 0.5)
        rx2 = random.randint(match2.x + margin2_x, match2.x + match2.w - margin2_x)
        ry2 = random.randint(match2.y + margin2_y, match2.y + match2.h - margin2_y)
        # scr.dragDrop(Location(rx1,ry1), Location(rx2,ry2))
        realistic_drag(Location(rx1,ry1), Location(rx2,ry2))
        return True
    return False
    
"""
def click_random_img_repeat(img, count, start, end):
    wait(1)
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(0.8))
    if match:
        # Create a dynamic margin (10% of the image's width and height)
        margin_x = int(match.w * 0.1)
        margin_y = int(match.h * 0.1)
        # Add the margin to the minimums, and subtract it from the maximums
        rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
        ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
        match.highlight(random.uniform(0.1, 1.0))
        for i in range(count):
            wait_random(start, end)
            scr.click(Location(rx,ry))
            # scr.click(img)
        return True
    print("failed to find: "+img)
    return False
"""


def click_random_img_searcharea_below(anchor_img, img, px, anchor_similarity=0.8, img_similarity=0.8, auto_wait_timeout=3):
    setAutoWaitTimeout(auto_wait_timeout)
    wait(random.uniform(0.5, 1.0))
    scr = Screen(screen)
    anchor = scr.exists(Pattern(anchor_img).similar(anchor_similarity))# checks if anchor exists on screen
    if anchor:
        anchor.highlight(random.uniform(0.1, 0.5))
        search_area = anchor.below(px) # creates search area based on anchor
        match = search_area.exists(Pattern(img).similar(img_similarity)) # checks if img exists in search area
        if match:
            # Create a dynamic margin (10% of the image's width and height)
            margin_x = int(match.w * 0.1)
            margin_y = int(match.h * 0.1)
            # Add the margin to the minimums, and subtract it from the maximums
            rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
            ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
            match.highlight(random.uniform(0.1, 0.5))
            scr.click(Location(rx,ry))
            return True
        else:
            print("failed to find: "+img)
            return False
    print("failed to find anchor: "+anchor_img)
    return False

def exists_similar_img(img, similarity=0.8, auto_wait_timeout=2):
    setAutoWaitTimeout(auto_wait_timeout)
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(similarity))
    if match:
        match.highlight(0.1, "blue")
        return True
    else:
        print("img does not exist: "+img)
        return False

def exist_similar_img_searcharea_below(anchor_img, img, px, similarity=0.8, auto_wait_timeout=2):
    setAutoWaitTimeout(auto_wait_timeout)
    scr = Screen(screen)
    anchor = scr.exists(Pattern(anchor_img).similar(similarity))# checks if anchor exists on screen
    if anchor:
        anchor.highlight(0.1, "blue")
        search_area = anchor.below(px) # creates search area based on anchor
        match = search_area.exists(Pattern(img).similar(similarity)) # checks if img exists in search area
        if match:
            match.highlight(0.1, "blue")
            return True
        else:
            print("failed to find: "+img)
            return False
    print("failed to find anchor: "+anchor_img)
    return False

"""
def click_random_word(word):
    scr = Screen(screen)
    match = scr.existsText(word)
    if match:
        rx = random.randint(match.x, match.x + match.w)
        ry = random.randint(match.y, match.y + match.h)
        scr.click(Location(rx,ry))
        return True
    print("failed to find: "+word)
    return False
"""


def realistic_drag(loc1, loc2, steps=50): # AI
    Settings.MoveMouseDelay = 0
    # 1. Initial movement and "Grip"
    mouseMove(loc1)
    wait(random.uniform(0.2, 0.4))
    mouseDown(Button.LEFT)
    wait(0.1) # Small pause to "engage" the drag
    
    # 2. Travel Loop
    for i in range(1, steps + 1):
        pct = float(i) / steps
        
        # Calculate the direct line
        target_x = loc1.x + (loc2.x - loc1.x) * pct
        target_y = loc1.y + (loc2.y - loc1.y) * pct
        
        # The Arc: math.sin produces a curve that peaks at 50% progress
        # 20 is the "height" of the arc in pixels
        arc_offset = math.sin(pct * math.pi) * 20 
        
        # Move the mouse (Subtract arc_offset to curve 'upwards')
        mouseMove(Location(int(target_x), int(target_y - arc_offset)))
        
        # 3. Variable Timing (Humans are slower at the start and end)
        if pct < 0.2 or pct > 0.8:
            wait(random.uniform(0.0003, 0.0008)) # Slow zones
        else:
            wait(random.uniform(0.0001, 0.0005)) # Fast zone (middle of drag)

    # 4. Release
    wait(random.uniform(0.1, 0.3))
    mouseUp(Button.LEFT)
    Settings.MoveMouseDelay = 0.5
