# Blake Automator

> A fast, modern automation tool for Windows - built for power users.

---

## Features

- Auto Clicker - Repeated clicking or hold-button mode with custom intervals
- Keyboard Presser - Auto-press any key at any speed
- Custom Hotkeys - Record any key as your toggle hotkey
- Themes - Switch between Dark / Light mode and color accents (Blue, Dark-Blue, Green)
- Settings Persistence - All settings saved between sessions
- Auto-Updater - Automatically checks for and downloads new versions on launch

---

## How to Use

1. **Download** `BlakeAutomator.exe` from the [latest release](https://github.com/sheluvsblakefrfr/blake-automator/releases/latest)
2. **Run it** - no installation required
3. Pick **Auto Clicker** or **Keyboard Presser** from the home screen
4. Configure your settings and hotkey
5. Press your hotkey anywhere - even in-game - to toggle on/off

---

## Configuration

All settings are saved to `ba_config.json` in the same folder as the `.exe`.

| Setting | Default | Description |
|---|---|---|
| Theme | Dark | Dark / Light / System |
| Color Accent | blue | blue / dark-blue / green |
| Click Hotkey | F6 | Toggle auto clicker |
| Press Hotkey | F7 | Toggle keyboard presser |
| Click Interval | 0.1s | Time between clicks |
| Press Interval | 0.1s | Time between key presses |

---


## Auto-Updater

On every launch, Blake Automator checks this repo's `version.txt` for a newer version. If one is found, you'll get a popup to download and install it automatically.

---

## Running from Source

**Requirements:**
- Python 3.10+
- `pip install customtkinter pyautogui pynput requests`

```bash
python blake_automator.py
```

**Build your own .exe:**
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name "BlakeAutomator" blake_automator.py
```

---

## License

This project is licensed under the GNU General Public License v3.0.

---

*Made with love by sheluvsblakefrfr*
