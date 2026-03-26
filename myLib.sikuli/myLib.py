from sikuli import *
import random

# Default Similarity Score is 0.7 (70%)
# General
screen = 1
Settings.MoveMouseDelay = .5
Settings.AutoWaitTimeout = 3 # looks for images for 3 seconds
Settings.OcrTextRead = True
Settings.OcrTextSearch = True

def wait_random(start, end): # start, end arguments are int
    sleep_time = random.uniform(start,end)
    wait(sleep_time)

def click_random_img(img, similarity=0.8, repeat=1, rand_start=0.0, rand_end=0.0):
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
        # wait_random(.5,1.5)
        match.highlight(0.1) # Highlights area detected, also acts like a sleep function
        for i in range(repeat):
            wait_random(rand_start, rand_end)
            scr.click(Location(rx,ry))
        wait(random.uniform(0.5, 1.0)) # wait for screen to load before next detection
        return True
    print("failed to find: "+img)
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


def click_random_img_searcharea_below(anchor_img, img, px):
    wait(random.uniform(0.5, 1.0))
    scr = Screen(screen)
    anchor = scr.exists(Pattern(anchor_img).similar(.99))# checks if anchor exists on screen
    if anchor:
        anchor.highlight(random.uniform(0.1, 0.5))
        search_area = anchor.below(px) # creates search area based on anchor
        match = search_area.exists(Pattern(img).similar(.8)) # checks if img exists in search area
        if match:
            # Create a dynamic margin (10% of the image's width and height)
            margin_x = int(match.w * 0.1)
            margin_y = int(match.h * 0.1)
            # Add the margin to the minimums, and subtract it from the maximums
            rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
            ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
            # wait_random(1,2)
            match.highlight(random.uniform(0.1, 0.5))
            scr.click(Location(rx,ry))
            return True
        else:
            print("failed to find: "+img)
            return False
    print("failed to find anchor: "+anchor_img)
    return False

def exists_similar_img(img, similarity=0.8):
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(similarity))
    if match:
        match.highlight(.5, "blue")
    else:
        print("img does not exist: "+img)
    return match


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