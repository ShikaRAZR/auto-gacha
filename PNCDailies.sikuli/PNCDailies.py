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
def auto_dailies_1():
    # Upgrade Doll with Combat EXP Once
    if not click_random_img("doll-info.png"):
        click_random_img("menu-top.png")
        click_random_img("menu-top-doll-info.png")
    wait(3)
    while exists_similar_img("doll-sort-low-level.png", similarity=0.99) is None:
        click_random_img("doll-sort-level.png")
    click_random_img("doll-select-specific.png")
    wait(1)
    if not click_random_img("doll-exp.png"):
        click_random_img("doll-breakthrough.png")
        click_random_img("doll-confirm.png")
    # Collect Oasis Resources Once
    click_random_img("menu-top.png")
    click_random_img("menu-top-oasis-collect.png")
    wait(3)
    # Complete 2 Resource Collections (Dorm)
    drag_random_img_to_dst("menu-top-operation-system.png", "menu-top-main-system.png")
    click_random_img("menu-top-dorm.png")
    wait(3)
    click_random_img("dorm-collect-resources.png")
    # Complete 1 Factory Order
    click_random_img("menu-top.png")
    click_random_img("menu-top-factory.png")
    wait(3)
    click_random_img("factory-recieve-all.png")
    wait(1)
    click_random_img("menu-top-back.png")
    click_random_img("factory-repeat-order.png")

def auto_dailies_2():
    click_random_img("menu-top.png")
    drag_random_img_to_dst("menu-top-main-system.png", "menu-top-sub-system.png")
    wait(1)
    click_random_img("menu-top-explore.png")
    wait(2)
    # Clear Vulnerability Check Once
    click_random_img("vulnerability-check.png")
    click_random_img_searcharea_below("vulnerability-check-T5.png", "vulnerability-quick-battle.png", 100)
    click_random_img("vulnerability-confirm.png")
    wait(10)
    click_random_img("vulnerability-end-battle.png")
    click_random_img("menu-top-back.png")
    wait(1)
    # Attempt Fragment Search Twice
    click_random_img("fragment-search.png")
    click_random_img("fragment-doll-select.png")
    click_random_img("auto-battle.png")
    click_random_img("add.png", repeat=6, rand_start=0.1, rand_end=0.5)
    click_random_img("fragment-ready.png")
    wait(1)
    click_random_img("auto-battle-30.png")
    wait(70)
    click_random_img("fragment-confirm.png")
    click_random_img_searcharea_below("fragment-doll-select.png", "fragment-doll-select.png", 100)
    click_random_img("auto-battle.png")
    click_random_img("add.png", repeat=4, rand_start=0.1, rand_end=0.5)
    click_random_img("fragment-ready.png")
    wait(1)
    click_random_img("auto-battle-30.png")
    wait(50)
    click_random_img("fragment-confirm.png")
    click_random_img("menu-top-back.png")
    # Clear Exception Protocol Cleanup Once
    click_random_img("exception-protocol.png")
    click_random_img("exception-exploration-protocol.png")
    click_random_img("exception-ready.png")
    click_random_img("exception-start.png")
    wait(10)
    click_random_img("exception-planned-mode-off.png")
    click_random_img("exception-execute.png")
    wait(350)
    click_random_img("exception-back.png")
    wait(5)
    click_random_img("exception-rewards.png")
    while exists_similar_img("exception-rewards-tap.png") is not None:
        click_random_img("exception-rewards-tap.png")
    while exists_similar_img("exception-reward-box.png", similarity=0.99) is not None:
        click_random_img("exception-reward-box.png", similarity=0.99)
    click_random_img("exception-reward-box.png", repeat=4, rand_start=0.5, rand_end=1.0)
    click_random_img("menu-top-back.png")
    wait(1)
    click_random_img("menu-top-back.png")
    # Spend 150 Keys

def auto_dailies_3():
    # Supply Store
    click_random_img("menu-top.png")
    click_random_img("menu-top-supplies.png")
    wait(3)
    click_random_img("store-supply-pack.png")
    click_random_img("supply-pack-free.png")
    click_random_img("supply-pack-free-button.png")
    click_random_img("store-top.png", repeat=2, rand_start=0.5, rand_end=1.0)
    wait(1)
    click_random_img("store-supply-pack-selected.png")
    wheel(WHEEL_DOWN, 10)
    wait(2)
    click_random_img("store-special-supplies.png")
    while exists_similar_img("store-diggcoin.png") is not None:
        click_random_img("store-diggcoin.png")
        if not click_random_img("store-purchase.png"): # If clicking on coin no longer shows purchase menu, end loop
            break
        click_random_img("store-top.png", repeat=2, rand_start=0.5, rand_end=1.0)
        wait(1)
    
    # Neural Search Basic
    click_random_img("menu-top.png")
    click_random_img("menu-top-neural-search.png")
    wait(3)
    click_random_img("neural-search-arrow.png", repeat=4, rand_start=0.5, rand_end=1.0)
    
    if exists_similar_img("neural-basic-search-menu.png"):
        for i in range(10):
            click_random_img("neural-basic-search-pull.png")
            wait(2)
            if not click_random_img("neural-search-skip.png"): # If there is no skip button. no pulls are occuring so end loop
                click_random_img("neural-search-confirm.png")
                break
            wait(2)
            click_random_img("neural-search-tap.png")
            wait(2)
        
    
# Check Season Pass


# click_random_img(".png")
# auto_dailies_1()
# auto_dailies_2()
# auto_dailies_3()
