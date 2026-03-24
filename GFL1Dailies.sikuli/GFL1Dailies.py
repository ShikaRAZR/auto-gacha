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
    wait(.5) # wait 1 second for screen to load before detection
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
        match.highlight(random.uniform(0.1, 1.0)) # Highlights area detected, also acts like a sleep function
        for i in range(repeat):
            wait_random(rand_start, rand_end)
            scr.click(Location(rx,ry))
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
    wait(1)
    scr = Screen(screen)
    anchor = scr.exists(Pattern(anchor_img).similar(.99))# checks if anchor exists on screen
    if anchor:
        anchor.highlight(random.uniform(0.1, 1.0))
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
            match.highlight(random.uniform(0.1, 1.0))
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

# Girl's Frontline - 1080p, windows 11, mumuplayer, gfl snap on top right
data_mode = 2 # Basic = 1, Intermediate = 2, Advanced = 3
def do_combat_simulation_1():

    # Go to Combat Simulation
    if not click_random_img("main-combat.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-combat.png")
            click_random_img("combat-bottom.png")
    click_random_img("combat-simulation-unselected.png")

    # Data Mode
    click_random_img("data-mode.png")
    if data_mode == 1: 
        click_random_img("basic-training.png")
        click_random_img("add-simulation.png", repeat=12, rand_start=0.1, rand_end=0.5)
    if data_mode == 2: 
        click_random_img("intermediate-training.png")
        click_random_img("add-simulation.png", repeat=6, rand_start=0.1, rand_end=0.5)
    if data_mode == 3: 
        click_random_img("advanced-training.png")
        click_random_img("add-simulation.png", repeat=4, rand_start=0.1, rand_end=0.5)
    click_random_img("smart-sweep.png")
    click_random_img("ok-button.png")
    click_random_img("combat-bottom-2.png")

def do_combat_simulation_2():
    # Coalition Drill
    click_random_img("coalition-drill.png")
    found_in_searcharea = False
    found_in_searcharea = click_random_img_searcharea_below("petri-dish.png","coalition-drill-attack.png", 300)
    if not found_in_searcharea:
        found_in_searcharea = click_random_img_searcharea_below("training-keycode.png","coalition-drill-attack.png", 300)
    if not found_in_searcharea:
        found_in_searcharea = click_random_img_searcharea_below("rapid-growth-disk.png","coalition-drill-attack.png", 300)
    click_random_img("add-simulation.png", repeat=4, rand_start=0.1, rand_end=0.5)
    click_random_img("smart-sweep.png")
    click_random_img("ok-button.png")
    click_random_img("combat-bottom-2.png")
    click_random_img("back.png")

def auto_dailies_1():
    # Go to Research
    if not click_random_img("main-research.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-research.png")
            click_random_img("component-enhancement.png")
    # Perform 3 Enhancements or Developments.
    click_random_img("equipment-enhancement.png")
    click_random_img("select-equip.png")
    click_random_img("icon-equipment.png")
    for i in range(3):
        click_random_img("add-research.png")
        click_random_img("ok-button.png", similarity=0.7)
    # Perform Equipment or Fairy Calibration once.
    click_random_img("equipment-calibration.png")
    click_random_img("select-equip-2.png")
    click_random_img("icon-equipment.png")
    click_random_img("calibration-button.png")
    # Go to Main Menu
    click_random_img("back.png")
    
def auto_dailies_2():
    # Go to Shop
    click_random_img("main-shop")
    wait(5)
    # Collect 5 Hearts.
    while(exists_similar_img("icon-heart.png")):
        click_random_img("icon-heart.png")
    # Go to Dorm from Shop
    if click_random_img("menu-top.png", similarity=0.6):
        click_random_img("menu-top-dorm.png")
        wait(5)
    # Collect 5 Hearts.
    while(exists_similar_img("icon-heart.png", similarity=0.6)):
        click_random_img("icon-heart.png", similarity=0.6)
    # Go to Friend Dorms From Dorm
    if click_random_img("dorm-visit-button.png"):
        if click_random_img("dorm-my-friends.png"):
            click_random_img("dorm-visit-specific.png")
    wait(3)
    # Like 5 players' Dormitories.
    like_count=0
    while(like_count<5):
        wait(1)
        if click_random_img("dorm-like.png"):
            like_count+=1
        click_random_img("dorm-next.png")
        print("Like Count: "+str(like_count))
    # Go to Main Menu
    click_random_img("back.png", similarity=0.7)
    wait(2)
    if click_random_img("menu-top.png", similarity=0.7):
        click_random_img("menu-top-main-menu.png")
        


#do_combat_simulation_1()
#do_combat_simulation_2()
#auto_dailies_1()
#auto_dailies_2()




