import random

# General
screen = 1
Settings.MoveMouseDelay = .5
Settings.AutoWaitTimeout = 5 # looks for images for 5 seconds
Settings.OcrTextRead = True
Settings.OcrTextSearch = True

def wait_random(start, end): # start, end arguments are int
    sleep_time = random.uniform(start,end)
    wait(sleep_time)

def click_random_img(img):
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(0.8))
    if match:
        rx = random.randint(match.x, match.x + match.w)
        ry = random.randint(match.y, match.y + match.h)
        scr.click(Location(rx,ry))
        return True
    print("failed to find: "+img)
    return False

def click_random_img_repeat(img, count, start, end):
    scr = Screen(screen)
    match = scr.exists(Pattern(img).similar(0.8))
    if match:
        rx = random.randint(match.x, match.x + match.w)
        ry = random.randint(match.y, match.y + match.h)
        for i in range(count):
            wait_random(start, end)
            scr.click(Location(rx,ry))
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
    if click_random_img("combat-simulation-unselected.png"):
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
    # click_random_img("smart-sweep.png")


do_combat_simulation()