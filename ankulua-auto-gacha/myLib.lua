
-- Default Similarity Score is 0.7 (70%)
-- General
Settings:setCompareDimension(true, 1280) -- if your screenshots were from a 1280px wide screen
Settings:setScriptDimension(true, 1280) -- the resolution width of your current device

setAutoWaitTimeout(5) -- looks for images for 5 seconds


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

    setAutoWaitTimeout(auto_wait_timeout)

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
