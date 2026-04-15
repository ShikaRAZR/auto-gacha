from myLib import *
import os
set_game_img_folder("GFLImages")

# uv run --with opencv-python --with numpy GFLDailies.py

# Girl's Frontline - 720p, waydroid
def do_combat_simulation_1():
    data_mode = 3 # Basic = 1, Intermediate = 2, Advanced = 3
    # Go to Combat Simulation
    if not click_random_img("main-combat.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-combat.png")
            click_random_img("combat-bottom.png")
    wait(1)
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
    click_random_img("combat-bottom-3.png")

def do_combat_simulation_2():
    # Coalition Drill
    click_random_img("coalition-drill.png")
    found_in_searcharea = False
    found_in_searcharea = click_random_img_searcharea_below("petri-dish.png","coalition-drill-attack.png", 300, anchor_similarity=0.99)
    if not found_in_searcharea:
        found_in_searcharea = click_random_img_searcharea_below("training-keycode.png","coalition-drill-attack.png", 300, anchor_similarity=0.99)
    if not found_in_searcharea:
        found_in_searcharea = click_random_img_searcharea_below("rapid-growth-disk.png","coalition-drill-attack.png", 300, anchor_similarity=0.99)
    wait(1)
    click_random_img("add-simulation.png", repeat=4, rand_start=0.1, rand_end=0.5)
    click_random_img("smart-sweep.png")
    click_random_img("ok-button.png")
    click_random_img("combat-bottom-3.png")
    click_random_img("back.png")

def auto_dailies_1():
    # Go to Research
    if not click_random_img("main-research.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-research.png")
            click_random_img("component-enhancement.png")
    # Perform 3 Equipment or Fairy Enhancements.
    click_random_img("equipment-enhancement.png")
    click_random_img("select-equip.png")
    click_random_img("icon-equipment.png")
    for i in range(3):
        click_random_img("add-research.png")
        click_random_img("ok-button.png", similarity=0.6)
    # Perform Equipment or Fairy Calibration once.
    click_random_img("equipment-calibration.png")
    click_random_img("select-equip-2.png")
    click_random_img("icon-equipment.png")
    click_random_img("calibration-button.png")
    # Go to Main Menu
    click_random_img("back.png")
    wait(3)
    
def auto_dailies_2():
    # Go to Shop
    click_random_img("main-shop.png")
    wait(8)
    # Collect 5 Hearts. (Kalina Shop)
    while(exists_similar_img("icon-heart.png")):
        click_random_img("icon-heart.png")
    # Go to Dorm from Shop
    if click_random_img("menu-top.png", similarity=0.6):
        click_random_img("menu-top-dorm.png")
        wait(8)
    # Collect 5 Hearts. (Dorm)
    while(exists_similar_img("icon-heart.png", similarity=0.7)):
        click_random_img("icon-heart.png", similarity=0.7)
    # Go to Friend Dorms From Dorm
    if click_random_img("dorm-visit-button.png"):
        if click_random_img("dorm-my-friends.png"):
            wait(2)
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
        
def auto_dailies_3():
    # Go to Armory
    click_random_img("main-armory.png")
    wait(2)
    # Give a gift to a T-Doll or Coalition Unit.
    click_random_img("filter-button.png")
    click_random_img("filter-below-max.png")
    click_random_img("filter-confirm-button.png")
    click_random_img("select-doll.png")
    wait(2)
    click_random_img("add-doll-level.png")
    wait(1)
    click_random_img_searcharea_below("present-combat-report.png", "present.png", 100)
    wait(1)
    click_random_img("add-present.png", repeat=2, rand_start=0.1, rand_end=0.5)
    click_random_img("ok-button.png")
    click_random_img("back-doll.png")
    # Go to Combat Mission from Armory
    if click_random_img("menu-top.png"):
        click_random_img("menu-top-combat.png")
        wait(4)
        if not exists_similar_img("combat-mission-selected.png"):
            click_random_img("combat-mission-unselected.png", auto_wait_timeout=5)
        wait(1)
    # Complete an Auto-Battle.
    if not click_random_img("combat-chapter-1.png"):
        template_coord=exists_similar_img("combat-chapter-ep.png")
        rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
        scroll(rx,ry, distance_px= 200, repeat = 4, duration_ms = 300, direction = "up")
        wait(2)
        click_random_img("combat-chapter-1.png")
    wait(2)
    click_random_img("combat-normal-2.png")
    click_random_img("combat-chapter-1-1.png")
    click_random_img("auto-battle-button.png")
    click_random_img("activate-quick-battle.png")
    click_random_img("subtract-auto-battle.png", repeat=2, rand_start=0.1, rand_end=0.5)
    click_random_img("select-echelon.png")
    click_random_img("echelon-1.png")
    click_random_img("ok-button.png", similarity=0.7)
    click_random_img("combat-start-button.png")
    click_random_img("ok-button.png", similarity=0.7)
    '''
    if click_random_img("combat-chapter-1.png"):
        click_random_img("combat-normal-2.png")
        click_random_img("combat-chapter-1-1.png")
        click_random_img("auto-battle-button.png")
        click_random_img("activate-quick-battle.png")
        click_random_img("subtract-auto-battle.png", repeat=2, rand_start=0.1, rand_end=0.5)
        click_random_img("select-echelon.png")
        click_random_img("echelon-1.png")
        click_random_img("ok-button.png")
        click_random_img("combat-start-button.png")
        click_random_img("ok-button.png")
    if click_random_img("combat-chapter-13.png"):
        click_random_img("combat-normal-2.png")
        click_random_img("combat-chapter-13-1.png")
        click_random_img("auto-battle-button.png")
        click_random_img("activate-quick-battle.png")
        click_random_img("subtract-auto-battle.png", repeat=2, rand_start=0.1, rand_end=0.5)
        click_random_img("select-echelon.png")
        click_random_img("echelon-2.png")
        click_random_img("ok-button.png")
        click_random_img("select-echelon.png")
        click_random_img("echelon-3.png")
        click_random_img("ok-button.png")
        click_random_img("combat-start-button.png")
        click_random_img("ok-button.png")
    '''
    wait(3)
    # Go to Main Menu
    click_random_img("back.png")
    click_random_img("back-auto-battle.png")
    click_random_img("back.png")

def semi_dailies_1():
    if not click_random_img("main-combat.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-combat.png")
            click_random_img("combat-bottom.png")
    wait(3)
    if not exists_similar_img("combat-mission-selected.png"):
        click_random_img("combat-mission-unselected.png", auto_wait_timeout=3)
    # if chapter one is not clicked or is not selected, scroll to chapter 1
    if not click_random_img("combat-chapter-1.png") and exists_similar_img("combat-chapter-1-selected.png") is False:
        template_coord=exists_similar_img("combat-chapter-ep.png")
        rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
        scroll(rx,ry, distance_px= 200, repeat = 4, duration_ms = 300, direction = "up")
        wait(2)
        click_random_img("combat-chapter-1.png")
    wait(2)
    # Complete any 2 stages (Auto-Battles are not counted)
    # Use Support Echelons Twice.
    for i in range(2):
        click_random_img("combat-normal-2.png")
        click_random_img("combat-chapter-1-1.png")
        click_random_img("combat-normal-battle.png")
        wait(2)
        click_random_img("skip.png")
        click_random_img("command-post.png")
        click_random_img("echelon-1.png")
        click_random_img("ok-button.png")
        wait(2)
        click_random_img("start-operation.png")
        wait(2)
        click_random_img("command-post-crop-2.png", similarity=0.7)
        click_random_img("command-post-crop-2.png", similarity=0.7)
        click_random_img("resupply.png")
        click_random_img("planning-mode.png")
        click_random_img("command-post-crop.png")
        click_random_img("practice-drone.png")
        click_random_img("execute-plan.png")
        wait(35)
        click_random_img("command-post-crop-3.png")
        click_random_img("support-echelon.png")
        wait(4)
        click_random_img("echelon-day.png")
        click_random_img("ok-button.png")
        click_random_img("end-round.png")
        wait(15)
        click_random_img("skip.png")
        wait(3)
        click_random_img("battle-end-top.png", repeat=10, rand_start=0.5, rand_end=1.0)
        wait(5)
    click_random_img("back.png")



'''
do_combat_simulation_1()
do_combat_simulation_2()
auto_dailies_1()
auto_dailies_2()
auto_dailies_3()
semi_dailies_1()
'''

# Perform 3 Enhancements or Developments. (IN PROGRESS)
do_combat_simulation_1()
do_combat_simulation_2()
auto_dailies_1()
auto_dailies_2()
auto_dailies_3()
semi_dailies_1()

