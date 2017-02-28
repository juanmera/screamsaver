import Quartz
import os
import time
from playsound import playsound

while True:
    gc = Quartz.CGSessionCopyCurrentDictionary(); 
    if 'CGSSessionScreenIsLocked' in gc and gc['CGSSessionScreenIsLocked'] == 1:
        if 'kCGSSessionSecureInputPID' in gc and gc['CGSSessionScreenIsLocked'] > 0:
            os.system('osascript -e "set volume output volume 100"')  
            playsound('scream.wav')
    time.sleep(0.1)

