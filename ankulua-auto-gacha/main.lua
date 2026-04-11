dofile(scriptPath() .. "myLib.lua")


click_random_img("icon1.png")
wait(3)
drag_random_img_to_dst("icon1.png", "icon2.png")
wait(3)
click_random_img_searcharea_below("icon1.png", "icon2.png", 200)
wait(3)
exists_similar_img("icon1.png")
wait(3)
exist_similar_img_searcharea_below("icon1.png", "icon2.png", 200)