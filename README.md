# auto-gacha

Automating gacha dailies for certain games.

Program
- Sikulix (python, java)

### Main Features:
- Select which window to focus on for each respective game
- Check boxes to select which game to automate

---

### Girls' Frontline

- Combat Sim

1. Auto
- Perform 3 Enhancements or Developments.
- Perform Equipment or Fairy Calibration once.
- Like 5 players' Dormitories.
- Give a gift to a T-Doll or Coalition Unit.
- Complete an Auto-Battle.

2. Passive
- Complete 3 Combat Simulations (Not including Coalition Drills).
- Perform an exploration at the Foward Basecamp.
- Complete 3 Coalition Drills.
- Complete 3 Logistics Missions.

3. Semi
- Perform a Capture Operation (either a Standard Capture or Aided Capture).
- Complete any 2 stages (Auto-Battles are not counted)
- Perform 3 Resource Recoveries.
- Perform 4 Equipment Productions (Includes I.O.P. Special Orders). 

4. Ignore
- Rescure a total of 5 Dolls in any stage
- Obtain 6 Mobile Armor Components.
- Destroy 50 regular units in victorious battles.
- Win 8 Battles with S ranks


Collect 5 Hearts. ----
3 T-Doll Enhancments--
Use Support Echelons Twice. ----
Defeat Boss--
Perform 2 Doll Productions. ----

    Features:
    - Read actual dailies on mission/quest page
    - Say what was sucessfully done, what failed, what was skipped

---

### Later To-Do:

Girls'Frontline Neural Cloud
Arknights

---

### Requirements:
Runs on Linux Wayland/X11 (Maybe), Windows

---

### Setup SikuliX in VSCode
https://launchpad.net/sikuli/+download
- sikulixide-2.0.5-win.jar (separate ide)
- sikulixapi-2.0.5-win.jar (for vscode)

#### Run Script On Windows 
- Cancel script: CTRL + ALT + C
- (preference, place jar file and script folder in the same directory):
    
        java -jar .\sikulixapi-2.0.5-win.jar -r .\GFL1Dailies.sikuli\

---

### Research
Programs/Libraries found for automation: 
- Airtest Project (ADB, Android Debug Bridge)
- SikuliX
- PyAutoGUI
- OpenCV-Python
- RapidOCR
- YOLO26 (Deep Learning/AI)