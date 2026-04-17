# auto-gacha

Automating gacha dailies for certain games.

### Program/Requirements
- Python, OpenCV, ADB
- Waydroid

### Features:
- Check boxes to select which game to automate
- Say what was sucessfully done, what failed, what was skipped

---

### Setup Python + OpenCV + ADB
```
sudo pacman -S android-tools python uv
waydroid prop set persist.waydroid.adb true
waydroid session stop
waydroid show-full-ui
adb connect 192.168.240.112:5555
adb devices
waydroid status
```
> Initial Install

```
uv run --with opencv-python --with numpy opencvadb-auto-gacha/GFL1Dailies.py
uv run --with opencv-python --with numpy opencvadb-auto-gacha/PNCDailies.py
```
> Run macros

> Downloads tools, uv makes virtual environment in its own bin and runs the script (```uv cache clean``` to remove it)

---

<details>
<summary>Girls' Frontline</summary>

Passive
- Complete a total of 10 Logistics missions--

Daily
- Complete 12 Combat Simulations or Coalition Drills--
- Perform a total of 5 Forward Basecamp Explorations--

Weekly
- Perform a total of 8 productions of any kind (Doll, Equipment or Fairy)--
- Eliminate a total of 50 Normal Units--
- Eliminate 1 Boss Unit--
- Win 8 Battle with S ranks--

Ignore
- Capture a total of 15 nodes in Gray Zone Exploration
- Perform 1 purchase
- Perform a total of 8 Capture Operations (either Standard Captures or Aided)

Other
- Frontline Protocol Collect (Battlepass)
</details>

---

<details>
<summary>Project Neural Cloud</summary>

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
</details>

---

### Later To-Do:

Girls'Frontline Neural Cloud
Arknights

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

---

<details>
<summary>Discontinued</summary>

- Combat Sim-

1. Passive (Ignore)
- Complete 3 Combat Simulations (Not including Coalition Drills).
- Perform an exploration at the Foward Basecamp.
- Complete 3 Coalition Drills.
- Complete 3 Logistics Missions.

2. Auto
- Perform 3 Enhancements or Developments. (IN PROGRESS)
- Perform 3 Equipment or Fairy Enhancements.-
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

### Setup SikuliX in VSCode (Discontinued)
https://launchpad.net/sikuli/+download
- sikulixide-2.0.5-win.jar (separate ide)
- sikulixapi-2.0.5-win.jar (for vscode)

#### Run Script On Windows
- Cancel script: CTRL + ALT + C
- (preference, place jar file and script folder in the same directory):
    
        java -jar .\sikuli-auto-gacha\sikulixapi-2.0.5-win.jar -r .\sikuli-auto-gacha\GFL1Dailies.sikuli\
        java -jar .\sikuli-auto-gacha\sikulixapi-2.0.5-win.jar -r .\sikuli-auto-gacha\PNCDailies.sikuli\
> Windows

        java -jar ./ankulua-auto-gacha/sikulixapi-2.0.5-lux.jar -r ./ankulua-auto-gacha/GFL1Dailies.sikuli/
        java -jar ./ankulua-auto-gacha/sikulixapi-2.0.5-lux.jar -r ./ankulua-auto-gacha/PNCDailies.sikuli/
> Linux (X11 only i think)

---

### Setup AnkuLua in Waydroid (Discontinued)

https://github.com/casualsnek/waydroid_script
> Install magisk > Magisk Delta > Settings (Cog) > App-Hide the Magisk app

https://github.com/AnkuLua/AnkuLuaAPK
https://ankulua.boards.net/board/8/tutorials

sudo mount --bind ~/Documents/Scripts ~/.local/share/waydroid/data/media/0/Download/Scripts
> Mount (Doesnt Work)
> Import scripts

---

</details>