import tkinter as tk
import customtkinter as ctk
import pyautogui
import threading
import time
import sys
import os
import requests
from pynput import keyboard

# Initial Configuration
VERSION = "2.0.0"
UPDATE_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/blake_automator.py"

# Appearance Defaults
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class BlakeAutomator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Blake Automator v{VERSION}")
        self.geometry("700x500")
        
        # State Variables
        self.active_frame = None
        self.clicking = False
        self.pressing = False
        self.target_key = "a"
        self.click_button = "left"
        self.click_mode = "Repeated Click" # or "Hold Button"
        self.click_interval = 0.1
        self.press_interval = 0.1
        
        # Keybinds (using standard pynput strings)
        self.click_hk = '<f6>'
        self.press_hk = '<f7>'
        self.recording_for = None # None, 'click', or 'press'
        
        # Initialize UI & Hotkeys
        self._setup_frames()
        self.show_frame("home")
        self._setup_hotkeys()
        
        # Start Auto-Update Check
        threading.Thread(target=self._check_for_updates, daemon=True).start()

    # --- UPDATER LOGIC ---
    def _check_for_updates(self):
        try:
            # Placeholder check - replace with real URL when ready
            # response = requests.get(f"{UPDATE_URL}.version", timeout=5)
            # if response.status_code == 200 and response.text.strip() != VERSION:
            #     self.prompt_update()
            pass
        except:
            pass

    # --- HOTKEY LOGIC ---
    def _setup_hotkeys(self):
        if hasattr(self, 'listener'):
            self.listener.stop()
            
        try:
            self.listener = keyboard.GlobalHotKeys({
                self.click_hk: self.toggle_clicker,
                self.press_hk: self.toggle_presser
            })
            self.listener.start()
        except Exception as e:
            print(f"Hotkey Error: {e}")

    def on_press_record(self, key):
        if self.recording_for:
            try:
                # Convert key to pynput string format
                if hasattr(key, 'name'):
                    k_str = f'<{key.name}>'
                else:
                    k_str = key.char
                
                if self.recording_for == 'click':
                    self.click_hk = k_str
                    self.clicker_hk_btn.configure(text=f"Hotkey: {k_str}")
                else:
                    self.press_hk = k_str
                    self.presser_hk_btn.configure(text=f"Hotkey: {k_str}")
                
                self.recording_for = None
                self._setup_hotkeys()
                return False # Stop listener
            except:
                pass

    def start_recording(self, target):
        self.recording_for = target
        if target == 'click':
            self.clicker_hk_btn.configure(text="Press Any Key...")
        else:
            self.presser_hk_btn.configure(text="Press Any Key...")
            
        # Temporarily stop global listener to capture key
        record_listener = keyboard.Listener(on_press=self.on_press_record)
        record_listener.start()

    # --- MODES ---
    def toggle_clicker(self):
        self.clicking = not self.clicking
        if self.clicking:
            self.status_label.configure(text="Running: CLICKER", text_color="#55FF55")
            threading.Thread(target=self.run_clicker, daemon=True).start()
        else:
            self.status_label.configure(text="Running: IDLE", text_color="#AAAAAA")

    def toggle_presser(self):
        self.pressing = not self.pressing
        if self.pressing:
            self.status_label.configure(text="Running: PRESSER", text_color="#FF5555")
            threading.Thread(target=self.run_presser, daemon=True).start()
        else:
            self.status_label.configure(text="Running: IDLE", text_color="#AAAAAA")

    def run_clicker(self):
        pyautogui.PAUSE = 0
        if self.click_mode == "Repeated Click":
            while self.clicking:
                pyautogui.click(button=self.click_button)
                time.sleep(self.click_interval)
        else: # Hold Mode
            pyautogui.mouseDown(button=self.click_button)
            while self.clicking:
                time.sleep(0.1)
            pyautogui.mouseUp(button=self.click_button)

    def run_presser(self):
        pyautogui.PAUSE = 0
        # Sync variables from entries before starting
        try:
            self.target_key = self.key_entry.get()
            self.press_interval = float(self.press_interval_entry.get())
        except: pass
        
        while self.pressing:
            pyautogui.press(self.target_key)
            time.sleep(self.press_interval)

    # --- UI MANAGEMENT ---
    def _setup_frames(self):
        self.frames = {}
        
        # Sidebar (Shared across frames)
        self.sidebar = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.sidebar, text="BLAKE\nAUTOMATOR", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, padx=20, pady=30)
        
        self.nav_home = ctk.CTkButton(self.sidebar, text="Home", command=lambda: self.show_frame("home"), fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"))
        self.nav_home.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        self.status_label = ctk.CTkLabel(self.sidebar, text="Running: IDLE", font=ctk.CTkFont(size=12))
        self.status_label.grid(row=10, column=0, pady=20)

        # Home Frame
        self.f_home = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.f_home.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self.f_home, text="Welcome, Blake", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, pady=(40, 20))
        
        ctk.CTkButton(self.f_home, text="🖱️ Auto Clicker", height=60, font=ctk.CTkFont(size=16), command=lambda: self.show_frame("clicker")).grid(row=1, column=0, padx=50, pady=10, sticky="ew")
        ctk.CTkButton(self.f_home, text="⌨️ Keyboard Presser", height=60, font=ctk.CTkFont(size=16), command=lambda: self.show_frame("presser")).grid(row=2, column=0, padx=50, pady=10, sticky="ew")
        ctk.CTkButton(self.f_home, text="⚙️ Settings", height=60, font=ctk.CTkFont(size=16), command=lambda: self.show_frame("settings")).grid(row=3, column=0, padx=50, pady=10, sticky="ew")

        # Clicker Frame
        self.f_clicker = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.f_clicker.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self.f_clicker, text="Auto Clicker Settings", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, pady=20)
        
        self.click_mode_sw = ctk.CTkSegmentedButton(self.f_clicker, values=["Repeated Click", "Hold Button"], command=lambda v: setattr(self, 'click_mode', v))
        self.click_mode_sw.set("Repeated Click")
        self.click_mode_sw.grid(row=1, column=0, pady=10)

        self.click_btn_sel = ctk.CTkOptionMenu(self.f_clicker, values=["Left", "Right", "Middle"], command=lambda v: setattr(self, 'click_button', v.lower()))
        self.click_btn_sel.set("Left")
        self.click_btn_sel.grid(row=2, column=0, pady=10)

        self.click_speed_entry = ctk.CTkEntry(self.f_clicker, placeholder_text="Interval (0.1)")
        self.click_speed_entry.grid(row=3, column=0, pady=10)
        
        self.clicker_hk_btn = ctk.CTkButton(self.f_clicker, text=f"Hotkey: {self.click_hk}", fg_color="#3333BB", command=lambda: self.start_recording('click'))
        self.clicker_hk_btn.grid(row=4, column=0, pady=10)

        # Presser Frame
        self.f_presser = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.f_presser.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self.f_presser, text="Keyboard Presser Settings", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, pady=20)
        
        self.key_entry = ctk.CTkEntry(self.f_presser, placeholder_text="Key (e.g. 'a', 'space')")
        self.key_entry.grid(row=1, column=0, pady=10)
        self.key_entry.insert(0, "a")

        self.press_interval_entry = ctk.CTkEntry(self.f_presser, placeholder_text="Interval (0.1)")
        self.press_interval_entry.grid(row=2, column=0, pady=10)
        self.press_interval_entry.insert(0, "0.1")

        self.presser_hk_btn = ctk.CTkButton(self.f_presser, text=f"Hotkey: {self.press_hk}", fg_color="#BB3333", command=lambda: self.start_recording('press'))
        self.presser_hk_btn.grid(row=3, column=0, pady=10)

        # Settings Frame
        self.f_settings = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.f_settings.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self.f_settings, text="Application Settings", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, pady=20)
        
        ctk.CTkLabel(self.f_settings, text="Theme Mode:").grid(row=1, column=0, pady=(10, 0))
        self.theme_sel = ctk.CTkOptionMenu(self.f_settings, values=["Dark", "Light"], command=ctk.set_appearance_mode)
        self.theme_sel.grid(row=2, column=0, pady=10)

        ctk.CTkLabel(self.f_settings, text="Color Accent:").grid(row=3, column=0, pady=(10, 0))
        self.color_sel = ctk.CTkOptionMenu(self.f_settings, values=["blue", "green", "dark-blue"], command=ctk.set_default_color_theme)
        self.color_sel.grid(row=4, column=0, pady=10)
        
        ctk.CTkLabel(self.f_settings, text="Note: Color changes require restart.", font=ctk.CTkFont(size=10)).grid(row=5, column=0)

    def show_frame(self, name):
        if self.active_frame:
            self.active_frame.grid_forget()
        
        if name == "home": self.active_frame = self.f_home
        elif name == "clicker": self.active_frame = self.f_clicker
        elif name == "presser": self.active_frame = self.f_presser
        elif name == "settings": self.active_frame = self.f_settings
        
        self.active_frame.grid(row=0, column=1, sticky="nsew")

if __name__ == "__main__":
    app = BlakeAutomator()
    app.mainloop()
