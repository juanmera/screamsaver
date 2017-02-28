import Quartz
import os
import time
import argparse
from playsound import playsound

parser = argparse.ArgumentParser()
parser.add_argument('-v', default=100, type=int, description='volume')
args = parser.parse_args()

while True:
    gc = Quartz.CGSessionCopyCurrentDictionary(); 
    if 'CGSSessionScreenIsLocked' in gc and gc['CGSSessionScreenIsLocked'] == 1:
        if 'kCGSSessionSecureInputPID' in gc and gc['CGSSessionScreenIsLocked'] > 0:
            snap_name = time.time()
            os.system('imagesnap -q -w 1 snaps/%d-after.jpg &' % snap_time)
            os.system('imagesnap -q -w 2 snaps/%d-before.jpg &' % snap_time)
            os.system('osascript -e "set volume output volume %d"' % args.v)  
            playsound('scream.wav')
    time.sleep(0.1)

