
-- Default Similarity Score is 0.7 (70%)
-- General
Settings:setCompareDimension(true, 1280) -- if your screenshots were from a 1280px wide screen
Settings:setScriptDimension(true, 1280) -- the resolution width of your current device
Settings:set("AutoWaitTimeout", 5) -- looks for images for 5 seconds


function wait_random(start_time, end_time) -- start, end arguments are int
    -- math.random() is a float between 0 and 1
    local sleep_time = start_time + math.random() * (end_time - start_time)
    wait(sleep_time)
end


function click_random_img(img, similarity, repeat_count, rand_start, rand_end, auto_wait_timeout)
    local similarity=similarity or 0.8
    local repeat_count=repeat_count or 1
    local rand_start=rand_start or 0.0
    local rand_end=rand_end or 0.0
    local auto_wait_timeout=auto_wait_timeout or 5

    Settings:set("AutoWaitTimeout", auto_wait_timeout)

    local match = exists(Pattern(img):similar(similarity)) -- check if img exists on screen, can be 80% similar 
    if match then
        -- Randomize area of clicking on the image
        -- Create a dynamic margin (10% of the image's width and height)
        local margin_x = math.floor(match:getW() * 0.1)
        local margin_y = math.floor(match:getH() * 0.1)
        -- Add the margin to the minimums, and subtract it from the maximums
        local rx = math.random(match:getX() + margin_x, match:getX() + match:getW() - margin_x)
        local ry = math.random(match:getY() + margin_y, match:getY() + match:getH() - margin_y)
        match:highlight(0.1) -- Highlights area detected, also acts like a sleep function
        for i=1,repeat_count do
            if rand_end>0 then
                wait_random(rand_start,rand_end)
            end
            click(Location(rx,ry))
        end
        wait_random(0.5,1.0) -- wait for screen to load before next detection
        return true
    end
    print("failed to find: " .. img)
    return false
end


function drag_random_img_to_dst(img1, img2, similarity) -- Drag Img to Destination
    local similarity=similarity or 0.8
    local match1 = exists(Pattern(img1):similar(similarity))
    local match2 = exists(Pattern(img2):similar(similarity))
    if match1 and match2 then
        local margin1_x = math.floor(match1:getW() * 0.5)
        local margin1_y = math.floor(match1:getH() * 0.5)
        local rx1 = math.random(match1:getX() + margin1_x, match1:getX() + match1:getW() - margin1_x)
        local ry1 = math.random(match1:getY() + margin1_y, match1:getY() + match1:getH() - margin1_y)
        local margin2_x = math.floor(match2:getW() * 0.5)
        local margin2_y = math.floor(match2:getH() * 0.5)
        local rx2 = math.random(match2:getX() + margin2_x, match2:getX() + match2:getW() - margin2_x)
        local ry2 = math.random(match2:getY() + margin2_y, match2:getY() + match2:getH() - margin2_y)
        realistic_drag(Location(rx1,ry1), Location(rx2,ry2))
        return true
    end
    return false
end


function click_random_img_searcharea_below(anchor_img, img, px, anchor_similarity, img_similarity, auto_wait_timeout)
    local anchor_similarity=anchor_similarity or 0.8
    local img_similarity=img_similarity or 0.8
    local auto_wait_timeout=auto_wait_timeout or 3
    Settings:set("AutoWaitTimeout", auto_wait_timeout)
    wait_random(0.5, 1.0)
    local anchor = exists(Pattern(anchor_img):similar(anchor_similarity)) -- checks if anchor exists on screen
    if anchor then
        anchor:highlight(0.1)
        -- start bottom left of anchor with x axis 20% more to left
        local ax = anchor:getX() - math.floor(anchor:getW() * 0.3)
        local ay = anchor:getY() + anchor:getH()
        --width 40% more to the right of original image for search area resulting in 20% padding on both sides
        local aw = math.floor(anchor:getW() * 1.6)
        -- creates search area with the height of px
        local search_area = Region(ax, ay, aw, px)
        search_area:highlight(0.1)
        local match = search_area:exists(Pattern(img):similar(img_similarity)) -- checks if img exists in search area
        if match then
            -- Create a dynamic margin (10% of the image's width and height)
            local margin_x = math.floor(match:getW() * 0.1)
            local margin_y = math.floor(match:getH() * 0.1)
            -- Add the margin to the minimums, and subtract it from the maximums
            local rx = math.random(match:getX() + margin_x, match:getX() + match:getW() - margin_x)
            local ry = math.random(match:getY() + margin_y, match:getY() + match:getH() - margin_y)
            match:highlight(0.1)
            click(Location(rx,ry))
            return true
        else
            print("failed to find: " .. img)
            return false
        end
    end
    print("failed to find anchor: " .. anchor_img)
    return false
end


function exists_similar_img(img, similarity, auto_wait_timeout)
    local similarity=similarity or 0.8
    local auto_wait_timeout=auto_wait_timeout or 2
    Settings:set("AutoWaitTimeout", auto_wait_timeout)
    local match = exists(Pattern(img):similar(similarity))
    if match then
        match:highlight(1.5)
        match:highlight(1.5)
        match:highlight(1.5)
        return true
    else
        print("img does not exist: " .. img)
        return false
    end
end

function exist_similar_img_searcharea_below(anchor_img, img, px, similarity, auto_wait_timeout)
    local similarity=similarity or 0.8
    local auto_wait_timeout=auto_wait_timeout or 2
    Settings:set("AutoWaitTimeout", auto_wait_timeout)
    local anchor = exists(Pattern(anchor_img):similar(similarity)) -- checks if anchor exists on screen
    if anchor then
        anchor:highlight(0.1)
        -- start bottom left of anchor with x axis 20% more to left
        local ax = anchor:getX() - math.floor(anchor:getW() * 0.3)
        local ay = anchor:getY() + anchor:getH()
        --width 40% more to the right of original image for search area resulting in 20% padding on both sides
        local aw = math.floor(anchor:getW() * 1.6)
        -- creates search area with the height of px
        local search_area = Region(ax, ay, aw, px)
        search_area:highlight(0.1)
        local match = search_area:exists(Pattern(img):similar(similarity)) -- checks if img exists in search area
        if match then
            match:highlight(1.5)
            match:highlight(1.5)
            match:highlight(1.5)
            return true
        else
            print("failed to find: " .. img)
            return false
        end
    end
    print("failed to find anchor: " .. anchor_img)
    return false
end


function realistic_drag(loc1, loc2, steps)
    local steps = steps or 50
    wait_random(0.2, 0.4)
    swipe(loc1, loc2)
end

--[[
function realistic_drag(loc1, loc2, steps) -- AI
    local steps=steps or 50
    -- 1. Initial movement and "Grip"
    mouseMove(loc1)
    wait_random(0.2, 0.4)
    mouseDown(Button.LEFT)
    wait(0.1) -- Small pause to "engage" the drag
    
    -- 2. Travel Loop
    for i=1, steps do
        local pct = i / steps
        
        -- Calculate the direct line
        local target_x = loc1:getX() + (loc2:getX() - loc1:getX()) * pct
        local target_y = loc1:getY() + (loc2:getY() - loc1:getY()) * pct
        
        -- The Arc: math.sin produces a curve that peaks at 50% progress
        -- 20 is the "height" of the arc in pixels
        local arc_offset = math.sin(pct * math.pi) * 20 
        
        -- Move the mouse (Subtract arc_offset to curve 'upwards')
        mouseMove(Location(math.floor(target_x), math.floor(target_y - arc_offset)))
        
        -- 3. Variable Timing (Humans are slower at the start and end)
        if pct < 0.2 or pct > 0.8 then
            wait(0.0003 + math.random() * (0.0008 - 0.0003)) -- Slow zones
        else
            wait(0.0001 + math.random() * (0.0005 - 0.0001)) -- Fast zone (middle of drag)
        end
    end
    -- 4. Release
    wait(0.1 + math.random() * (0.3 - 0.1))
    mouseUp(Button.LEFT)
end
]]--
