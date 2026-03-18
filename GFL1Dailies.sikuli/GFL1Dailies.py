import random

# Default Similarity Score is 0.7 (70%)
# General
screen = 3
Settings.MoveMouseDelay = .5
Settings.AutoWaitTimeout = 5 # looks for images for 5 seconds
Settings.OcrTextRead = True
Settings.OcrTextSearch = True

def wait_random(start, end): # start, end arguments are int
    sleep_time = random.uniform(start,end)
    wait(sleep_time)

def click_random_img(img):
    scr = Screen(screen) # Set screen to search for img
    match = scr.exists(Pattern(img).similar(0.8)) # check if img exists on screen, can be 80% similar 
    if match:
        # Create a dynamic margin (10% of the image's width and height)
        margin_x = int(match.w * 0.1)
        margin_y = int(match.h * 0.1)
        # Add the margin to the minimums, and subtract it from the maximums
        rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
        ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
        wait_random(1,2)
        scr.click(Location(rx,ry))
        return True
    print("failed to find: "+img)
    return False

def click_random_img_searcharea_below(anchor_img, img, px):
    scr = Screen(screen)
    anchor = scr.exists(Pattern(anchor_img).similar(.99))# checks if anchor exists on screen
    if anchor:
        search_area = anchor.below(px) # creates search area based on anchor
        match = search_area.exists(Pattern(img).similar(.8)) # checks if img exists in search area
        if match:
            # Create a dynamic margin (10% of the image's width and height)
            margin_x = int(match.w * 0.1)
            margin_y = int(match.h * 0.1)
            # Add the margin to the minimums, and subtract it from the maximums
            rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
            ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
            wait_random(1,2)
            scr.click(Location(rx,ry))
            return True
        else:
            print("failed to find: "+img)
            return False
    print("failed to find anchor: "+anchor_img)
    return False

def exists_similar_img(img):
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(0.8))
    return match

def click_random_img_repeat(img, count, start, end):
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(0.8))
    if match:
        # Create a dynamic margin (10% of the image's width and height)
        margin_x = int(match.w * 0.1)
        margin_y = int(match.h * 0.1)
        # Add the margin to the minimums, and subtract it from the maximums
        rx = random.randint(match.x + margin_x, match.x + match.w - margin_x)
        ry = random.randint(match.y + margin_y, match.y + match.h - margin_y)
        for i in range(count):
            wait_random(start, end)
            # scr.click(Location(rx,ry))
            scr.click(img)
        return True
    print("failed to find: "+img)
    return False

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

# Girl's Frontline - 1080p, windows 11, mumuplayer, gfl snap on top right
data_mode = 1 # Basic = 1, Intermediate = 2, Advanced = 3
def do_combat_simulation():
    if not click_random_img("combat-button.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-combat.png")
            click_random_img("combat-bottom.png")
    click_random_img("combat-simulation-unselected.png")
    click_random_img("data-mode.png")
    if data_mode == 1: 
        click_random_img("basic-training.png")
        click_random_img_repeat("simulation-add.png", 12, 0, .5)
    if data_mode == 2: 
        click_random_img("intermediate-training.png")
        click_random_img_repeat("simulation-add.png", 6, 0, .5)
    if data_mode == 3: 
        click_random_img("advanced-training.png")
        click_random_img_repeat("simulation-add.png", 4, 0, .5)
    click_random_img("smart-sweep.png")
    click_random_img("ok-button.png")
    click_random_img("combat-bottom-2.png")

def do_combat_simulation_2():
    click_random_img("coalition-drill.png")
    found_in_searcharea = False
    found_in_searcharea = click_random_img_searcharea_below("petri-dish.png","coalition-drill-attack.png", 300)
    if not found_in_searcharea:
        found_in_searcharea = click_random_img_searcharea_below("training-keycode.png","coalition-drill-attack.png", 300)
    if not found_in_searcharea:
        found_in_searcharea = click_random_img_searcharea_below("rapid-growth-disk.png","coalition-drill-attack.png", 300)
    click_random_img_repeat("simulation-add.png", 4, 0, .5)
    click_random_img("smart-sweep.png")
    click_random_img("ok-button.png")
    click_random_img("combat-bottom-2.png")


do_combat_simulation()
do_combat_simulation_2()
