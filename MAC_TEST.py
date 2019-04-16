import netifaces
import os
import time
import sys
import subprocess
import socket

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
        subprocess.Popen
        return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, env={'PATH': os.getenv('PATH')}).stdout.decode('utf-8')

    def populate_MAC_Dict(self):
        output = self.run_command(['arp', '-a'])
        # TODO: Use regex to split up into a dict of IP's and MAC addresses, then build dicts with the results

util = utils()

# Tests the run_command method to check that it can in fact run a command & return the result
print(util.run_command(['pip --help']))
print(util.run_command(['spoof-mac.py list']))
# TODO: npm install spoof and set up command line argument methods in here so it is effectivly put into python!
#arp = os.system('arp -a')
#os.system('spoof-mac.py list')

print("TEST \n",util.run_command(['arp', '-a']))

def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 

get_Host_name_IP()

# Try at shcool?

#TODO: Set up so we get names aswell of known IP's?
ip = '192.168.206.1'
dns = socket.gethostbyaddr(ip)
print("Name of device @:"+ip, dns[0])

# Trying to associate a device name with a known ip
#print("TEST \n",util.run_command(['nslookup', ip]))

# TODO: Denies access due to the fact that is is under system 32. Solution? Move clone the spoof-mac.py project into here to use. (Only worry about this if trying to spoof MAC address)
#print("TEST \n",util.run_command(['spoof-mac.py', 'list']))

#pip install SpoofMAC
#spoof-mac.py list