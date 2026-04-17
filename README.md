# Blake Automator v4

> A fast, modern premium automation suite for Windows — built for power users.

![Blake Automator]

---

## 🚀 Features (v4.0.0 Update)

- 🖱️ **Auto Clicker** — Repeated clicking or hold-button mode with fixed intervals or advanced anti-ban randomization.
- ⌨️ **Keyboard Auto** — Auto-press any keystroke dynamically at any randomized or fixed speed.
- 📜 **Macro Recorder** — Record full sequences of inputs, adjust their precise delays, and play them back in infinite loops.
- 🎯 **Advanced Hotkeys** — Assign any key as your global toggle hotkey with instant auto-cancellations so inputs don't glitch.
- 🛡️ **Anti-Ban Humanizer** — Integrated ±15% randomization and randomized interval modes to bypass repetitive-input detection.
- 🎨 **Premium UI Themes** — Switch between a resizable Dark/Light mode layout and color accents.
- 💾 **Profile Management** — All configurations are automatically managed, and you can create endless profiles to switch between scripts.
- 🔄 **Auto-Updater** — Automatically checks for and applies new versions on launch seamlessly.

---

## 🛠️ How to Use

1. **Download** `BlakeAutomater_v4.0.0.ZIP` from the [latest release](https://github.com/sheluvsblakefrfr/blake-automator/releases/latest)
2. **Run it** — no installation required!
3. Pick **Auto Clicker**, **Keyboard Auto**, or **Macro Recorder** from the sleek sidebar.
4. Set your target keys, speed delays, and humanizer settings.
5. Record your ON/OFF toggle hotkey (`[✖]` to clear it).
6. Press your hotkey anywhere — even minimized in system tray — to seamlessly start overriding your system!

---

## ⚙️ Configuration

All user settings are completely local and automatically saved to `ba_config.json` in the same directory as the `.exe`. Never worry about configuring your anti-ban delays more than once!

---

## 👨‍💻 Running from Source

**Requirements:**
- Python 3.10+
- `pip install customtkinter pyautogui pynput requests pystray pillow`

```bash
python blake_automator.py
```

**Build your own `.exe` locally:**
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon "icon.ico" --name "BlakeAutomator" blake_automator.py
```

---

## 📜 License

This project is open-source under the **GNU General Public License v3.0**.  

---

*Made by **Sheluvsblakefrfrv2** on Discord.*
