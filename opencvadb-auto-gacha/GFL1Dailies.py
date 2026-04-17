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
    # Complete 12 Combat Simulations or Coalition Drills
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
    # Complete 12 Combat Simulations or Coalition Drills
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
    if click_random_img("menu-top.png"):
        click_random_img("menu-top-main-menu.png")
    wait(3)


def auto_dailies_1():
    # Go to Shop
    click_random_img("main-shop.png")
    wait(5)
    # Collect 5 Hearts. (Kalina Shop)
    while(exists_similar_img("icon-heart.png")):
        click_random_img("icon-heart.png")
    if click_random_img("menu-top.png", similarity=0.6):
        click_random_img("menu-top-forward-basecamp.png")
    wait(2)
    # Perform a total of 5 Forward Basecamp Explorations
    click_random_img("forward-basecamp-explore.png")
    if exists_similar_img("cancel-button.png"):
        click_random_img("cancel-button.png")
    

def auto_weeklies_1():     
    # Perform a total of 8 productions of any kind (Doll, Equipment or Fairy)
    if not click_random_img("main-combat.png"):
        if click_random_img("menu-top.png"):
            if exists_similar_img("menu-top-dorm.png") and exists_similar_img("menu-top-capture-operation.png"):
                drag_random_img_to_dst("menu-top-dorm.png", "menu-top-capture-operation.png")
                click_random_img("menu-top-factory.png")
    wait(2)
    click_random_img("factory-tdoll-production.png")
    wait(1)
    if exists_similar_img("tdoll-production-collect-all.png"):
        click_random_img("tdoll-production-collect-all.png")
        if exists_similar_img("ok-button.png"):
            click_random_img("ok-button.png")
        click_random_img("tdoll-production-pull.png", repeat=16, rand_start=0.1, rand_end=0.5)
    wait(2)


def auto_weeklies_2():
    # Eliminate a total of 50 Normal Units
    # Eliminate 1 Boss Unit
    # Win 8 Battle with S ranks
    if not click_random_img("main-combat.png"):
        if click_random_img("menu-top.png"):
            click_random_img("menu-top-combat.png")
            click_random_img("combat-bottom.png")
    wait(3)
    click_random_img("combat-mission-unselected.png")
    # if chapter 0 is not clicked or is not selected, scroll to chapter 0
    if click_random_img("combat-chapter-0.png", similarity=0.95) is None and exists_similar_img("combat-chapter-0-selected.png") is None:
        template_coord=exists_similar_img("combat-chapter-ep.png")
        rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
        scroll(rx,ry, distance_px= 200, repeat = 4, duration_ms = 300, direction = "up")
        wait(2)
        click_random_img("combat-chapter-0.png", similarity=0.95)
    wait(1)
    click_random_img("combat-chapter-0-4.png")
    click_random_img("combat-normal-battle.png")
    wait(1)
    click_random_img("skip.png")
    # Mission
    wait(1)
    click_random_img("combat-heliport-1.png")
    click_random_img("echelon-1.png")
    click_random_img("ok-button.png")
    wait(1)
    click_random_img("combat-heliport-2.png")
    click_random_img("echelon-2.png")
    click_random_img("ok-button.png")
    wait(1)
    click_random_img("combat-heliport-3.png")
    click_random_img("echelon-3.png")
    click_random_img("ok-button.png")
    wait(1)
    click_random_img("combat-command-post.png")
    click_random_img("echelon-4-caution.png")
    click_random_img("ok-button.png")
    for i in range(2):
        wait(1)
        click_random_img("start-operation.png")
        # Resupply
        wait(2)
        click_random_img("combat-command-post-team.png", repeat = 2, rand_start=.5, rand_end=1)
        click_random_img("resupply.png")
        click_random_img("combat-scroll.png")
        wait(1)
        click_random_img("combat-heliport-1-team.png", repeat = 2, rand_start=.5, rand_end=1)
        click_random_img("resupply.png")
        click_random_img("combat-scroll.png")
        wait(1)
        click_random_img("combat-heliport-2-team.png", repeat = 2, rand_start=.5, rand_end=1)
        click_random_img("resupply.png")
        click_random_img("combat-scroll.png")
        wait(1)
        click_random_img("combat-heliport-3-team.png", repeat = 2, rand_start=.5, rand_end=1)
        click_random_img("resupply.png")
        click_random_img("combat-scroll.png")
        wait(1)
        click_random_img("planning-mode.png")
        click_random_img("combat-command-post-team.png")
        wait(2)
        # Scroll
        template_coord=exists_similar_img("combat-scroll.png")
        rx, ry = get_random_coordinates(template_coord[0], template_coord[1], template_coord[2], template_coord[3])
        scroll(rx,ry, distance_px= 400, repeat = 5, duration_ms = 300, direction = "down")
        click_random_img("combat-command-post-enemy.png")
        click_random_img("combat-next-round.png")
        click_random_img("execute-plan.png")
        wait(200)
        click_random_img("skip-2.png")
        wait(5)
        click_random_img("repeat-battle.png", repeat = 7, rand_start=.5, rand_end=1)
        click_random_img("skip.png")
    click_random_img("combat-select-operation.png")



#do_combat_simulation_1()
#do_combat_simulation_2()
auto_dailies_1()
#auto_weeklies_1()
#auto_weeklies_2()