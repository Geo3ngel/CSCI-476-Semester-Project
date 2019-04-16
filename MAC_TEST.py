import netifaces
import numpy as np
import sys
import os
import time
import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

print(netifaces.interfaces())

# initalize empty dictionary
mac_dict = {}

# fill dictionary with MAC Addresses associated w/ numbers

iter = 0

# make data structure object instead for a dist of objects containing an IP, MAC, and Device Name
for mac in netifaces.interfaces():
    mac_dict[mac] = iter
    iter+=1


print(mac_dict)

print("==================================================================================")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)

# Detects the operating system in use
operating_system = get_platform()
slowprint(operating_system + " operating system detected.")

# TODO: Make command versions for linux and macOS in addition to Windows