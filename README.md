# auto-gacha

Automating gacha dailies for certain games.

Program
- Sikulix (python, java)
- AnkuLua

### Main Features:
- Select which window to focus on for each respective game
- Check boxes to select which game to automate
- Say what was sucessfully done, what failed, what was skipped

---

### Girls' Frontline
- Combat Sim-

1. Passive
- Complete 3 Combat Simulations (Not including Coalition Drills).
- Perform an exploration at the Foward Basecamp.
- Complete 3 Coalition Drills.
- Complete 3 Logistics Missions.

2. Auto
- Perform 3 Enhancements or Developments.(FIX ENHANCE DOLLS NOT EQUIPMENT)
- Perform 3 Equipment or Fairy Enhancements.
- Perform Equipment or Fairy Calibration once.-
- Like 5 players' Dormitories.-
- Give a gift to a T-Doll or Coalition Unit.-
- Complete an Auto-Battle.-
- Collect 5 Hearts.-

3. Semi
- Perform a Capture Operation (either a Standard Capture or Aided Capture).
- Complete any 2 stages (Auto-Battles are not counted)-
- Perform 3 Resource Recoveries.
- Perform 4 Equipment Productions (Includes I.O.P. Special Orders). 
- Use Support Echelons Twice.-

4. Ignore
- Rescue a total of 5 Dolls in any stage
- Obtain 6 Mobile Armor Components.
- Destroy 50 regular units in victorious battles.
- Win 8 Battles with S ranks

3 T-Doll Enhancments--
Defeat Boss--
Perform 2 Doll Productions. ----

---

### Project Neural Cloud

Passive
- Log into the game
- Reach 50 Daily Activity

Auto
- Upgrade Doll with Combat EXP Once-
- Collect Oasis Resources Once-
- Complete 2 Resource Collections-
- Complete 1 Factory Order-
- Attempt Fragment Search Twice(100% PROGRESS MORE DOLLS)
- Clear Vulnerability Check Once-
- Spend 150 Keys-
- Clear Exception Protocol Cleanup Once-

Ignore
- Replenish Keys 1 time
- Clear Endless Exploration Once
- Attempt Algorithm Collection twice

Custom
- Neural Search Basic-
- Supply Store-
- Collect Rewards-
- Check Battle Pass-

---

### Later To-Do:

Girls'Frontline Neural Cloud
Arknights

---

### Setup SikuliX in VSCode
https://launchpad.net/sikuli/+download
- sikulixide-2.0.5-win.jar (separate ide)
- sikulixapi-2.0.5-win.jar (for vscode)

#### Run Script On Windows 
- Cancel script: CTRL + ALT + C
- (preference, place jar file and script folder in the same directory):
    
        java -jar .\sikuli\sikulixapi-2.0.5-win.jar -r .\sikuli\GFL1Dailies.sikuli\
        java -jar .\sikuli\sikulixapi-2.0.5-win.jar -r .\sikuli\PNCDailies.sikuli\
> Windows

        java -jar ./sikuli/sikulixapi-2.0.5-lux.jar -r ./sikuli/GFL1Dailies.sikuli/
        java -jar ./sikuli/sikulixapi-2.0.5-lux.jar -r ./sikuli/PNCDailies.sikuli/
> Linux

---
### Setup AnkuLua in Waydroid:

https://github.com/casualsnek/waydroid_script
> Install magisk > Magisk Delta > Settings (Cog) > App-Hide the Magisk app

https://github.com/AnkuLua/AnkuLuaAPK

---

### Research
Programs/Libraries found for automation: 
- Airtest Project (ADB, Android Debug Bridge)
- SikuliX
- AnkuLua
- PyAutoGUI
- OpenCV-Python
- RapidOCR
- YOLO26 (Deep Learning/AI)