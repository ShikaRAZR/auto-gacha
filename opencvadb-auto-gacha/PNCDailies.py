from myLib import *
import os
set_game_img_folder("PNCImages")

# uv run --with opencv-python --with numpy PNCDailies.py

# Project Neural Cloud - 720p, waydroid
def auto_dailies_1():
    print("-----------auto_dailies_1-----------")
    # Upgrade Doll with Combat EXP Once
    if not click_random_img("doll-info.png"):
        click_random_img("menu-top.png")
        click_random_img("menu-top-doll-info.png")
    wait(3)
    while not exists_similar_img("doll-sort-low-level.png", similarity=0.99):
        click_random_img("doll-sort-level.png")
    click_random_img("doll-select-specific.png")
    wait(1)
    if not click_random_img("doll-exp.png"):
        click_random_img("doll-breakthrough.png")
        click_random_img("doll-confirm.png")
    # Collect Oasis Resources Once
    click_random_img("menu-top.png")
    click_random_img("menu-top-oasis-collect.png")
    wait(5)
    # Complete 2 Resource Collections (Dorm)
    drag_random_img_to_dst("menu-top-operation-system.png", "menu-top-main-system.png")
    wait(1)
    click_random_img("menu-top-dorm.png")
    wait(3)
    click_random_img("dorm-collect-resources.png")
    # Complete 1 Factory Order
    click_random_img("menu-top.png")
    click_random_img("menu-top-factory.png")
    wait(3)
    if click_random_img("factory-recieve-all.png"):
        wait(1)
        click_random_img("menu-top-back.png")
        click_random_img("factory-repeat-order.png")

def auto_dailies_2():
    print("-----------auto_dailies_2-----------")
    click_random_img("menu-top.png")
    drag_random_img_to_dst("menu-top-operation-system.png", "menu-top-sub-system.png")
    wait(1)
    click_random_img("menu-top-explore.png")
    wait(5)
    click_random_img("resource.png")
    wait(1)
    # Clear Vulnerability Check Once
    click_random_img("vulnerability-check.png")
    click_random_img_searcharea_below("vulnerability-check-T5.png", "vulnerability-quick-battle.png", 100, anchor_similarity=0.9, img_similarity=0.9)
    click_random_img("vulnerability-confirm.png")
    wait(3)
    click_random_img("vulnerability-check-bottom.png", repeat=3, rand_start=0.5, rand_end=1.0)
    click_random_img("menu-top-back.png")
    wait(1)
    # Attempt Fragment Search Twice
    click_random_img("fragment-search.png")
    if click_random_img("fragment-doll-select.png", similarity=0.9):
        click_random_img("auto-battle.png")
        click_random_img("add.png", repeat=6, rand_start=0.1, rand_end=0.5)
        click_random_img("fragment-ready.png")
        wait(1)
        click_random_img("auto-battle-30.png")
        wait(70)
        click_random_img("fragment-confirm.png", auto_wait_timeout=15)
    if click_random_img_searcharea_below("fragment-doll-select.png", "fragment-doll-select.png", 300, anchor_similarity=0.9, img_similarity=0.9):
        click_random_img("auto-battle.png")
        click_random_img("add.png", repeat=4, rand_start=0.1, rand_end=0.5)
        click_random_img("fragment-ready.png")
        wait(1)
        click_random_img("auto-battle-30.png")
        wait(50)
        click_random_img("fragment-confirm.png", auto_wait_timeout=15)
    click_random_img("menu-top-back.png")
    # Clear Exception Protocol Cleanup Once
    click_random_img("exception-protocol.png")
    if not exists_similar_img("exception-complete.png"):
        click_random_img("exception-exploration-protocol.png")
        wait(1)
        click_random_img("exception-ready.png")
        wait(1)
        click_random_img("exception-start.png")
        wait(10)
        click_random_img("exception-planned-mode-off.png")
        click_random_img("exception-execute.png")
        wait(350)
        click_random_img("exception-back.png", auto_wait_timeout=15)
        wait(5)
        click_random_img("exception-rewards.png")
        while exists_similar_img("exception-rewards-tap.png", similarity=0.7):
            click_random_img("exception-rewards-tap.png", similarity=0.7)
        while exists_similar_img("exception-reward-box.png", similarity=0.99):
            click_random_img("exception-reward-box.png", similarity=0.99)
        click_random_img("exception-reward-box.png", repeat=4, rand_start=0.5, rand_end=1.0)
        click_random_img("menu-top-back.png")
        wait(1)
    click_random_img("menu-top-back.png")
    



def auto_dailies_3():
    print("-----------auto_dailies_3-----------")
    # Supply Store
    click_random_img("menu-top.png")
    click_random_img("menu-top-supplies.png")
    wait(5)
    click_random_img("store-supply-pack.png")
    if click_random_img("supply-pack-free.png", auto_wait_timeout=2):
        click_random_img("supply-pack-free-button.png")
        click_random_img("store-top.png", repeat=2, rand_start=0.5, rand_end=1.0)
        wait(1)
    if click_random_img("supply-pack-free-weekly.png", auto_wait_timeout=2):
        click_random_img("supply-pack-free-button.png")
        click_random_img("store-top.png", repeat=2, rand_start=0.5, rand_end=1.0)
        wait(1)
    '''
    if click_random_img("supply-pack-free-monthly.png", auto_wait_timeout=2):
        click_random_img("supply-pack-free-button.png")
        click_random_img("store-top.png", repeat=2, rand_start=0.5, rand_end=1.0)
        wait(1)
    '''
    template_coord=exists_similar_img("store-supply-pack-selected.png")
    rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
    scroll(rx,ry, distance_px= 200, repeat = 4, duration_ms = 300, direction = "down")

    wait(2)
    click_random_img("store-special-supplies.png")
    while exist_similar_img_searcharea_below("store-top-2.png", "store-diggcoin.png", 300) is not None:
        click_random_img_searcharea_below("store-top-2.png", "store-diggcoin.png", 300)
        wait(1)
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
            if not click_random_img("neural-search-skip.png", auto_wait_timeout=1): # If there is no skip button. no pulls are occuring so end loop
                click_random_img("neural-search-confirm.png")
                break
            wait(2)
            click_random_img("neural-search-tap.png")
            wait(2)
    # Collect Rewards 
    click_random_img("menu-top.png")
    while exists_similar_img("menu-top-claim-rewards.png"):
        click_random_img("menu-top-claim-rewards.png")
    click_random_img("menu-top-operation-system.png")
    # Check Battle Pass
    click_random_img("menu-top-battle-pass.png")
    wait(2)
    click_random_img("battle-pass-collect.png")
    click_random_img("battle-pass-confirm.png")
    click_random_img("battle-pass-bottom.png", repeat=3, rand_start=0.5, rand_end=1.0)

def auto_dailies_4():
    print("-----------auto_dailies_4-----------")
    if not exists_similar_img("menu-top-operation-system.png"):
        click_random_img("menu-top.png")
    click_random_img("menu-top-explore.png")
    wait(3)
    # Spend 150 Keys
    drag_random_img_to_dst("fragment-search.png", "vulnerability-check.png")
    wait(1)
    click_random_img("resource-collection.png", similarity=0.9)
    if click_random_img("resource-skill.png"):
        click_random_img("auto-battle.png")
        click_random_img("add.png")
        click_random_img("resource-ready.png")
        wait(3)
        click_random_img("auto-battle-30.png")
        wait(30)
        click_random_img("fragment-confirm.png", auto_wait_timeout=15)
    if click_random_img("resource-exp.png"):
        click_random_img("auto-battle.png")
        click_random_img("add.png", repeat=10, rand_start=0.1, rand_end=0.5)
        click_random_img("resource-ready.png")
        wait(3)
        click_random_img("auto-battle-30.png")
        wait(120)
        click_random_img("fragment-confirm.png", auto_wait_timeout=15)
    click_random_img("menu-top.png")

'''
click_random_img(".png")
auto_dailies_1()
auto_dailies_2()
auto_dailies_3()
auto_dailies_4()
'''

# Add monthly store png
auto_dailies_1()
auto_dailies_2()
auto_dailies_3()
auto_dailies_4()
print("-----------DONE-----------")

