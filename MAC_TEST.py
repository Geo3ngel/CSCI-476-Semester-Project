import netifaces
import os
import time
import sys
import subprocess

# TODO: Make command versions for linux and macOS in addition to Windows

class utils:

    def __init__(self, *args, **kwargs):
        self.operating_system = self.get_platform()
        self.slowprint(self.operating_system + " operating system detected.")
        
        # initalize empty dictionary
        self.mac_dict = {}

        return super().__init__(*args, **kwargs)

    # Informs us of what operating system is being used
    def get_platform(self):
        platforms = {
            'linux1' : 'Linux',
            'linux2' : 'Linux',
            'darwin' : 'OS X',
            'win32' : 'Windows'
        }
        if sys.platform not in platforms:
            return sys.platform
        
        return platforms[sys.platform]

    # Prints things slowly for style
    def slowprint(self, s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(3. / 100)

    # Attempts to run any string as a command
    def run_command(self, command):
        
        return subprocess.run([command], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')

util = utils()

# Tests the run_command method to check that it can in fact run a command & return the result
print(util.run_command('dir'))
# TODO: npm install spoof and set up command line argument methods in here so it is effectivly put into python!

#pip install SpoofMAC
#spoof-mac.py list