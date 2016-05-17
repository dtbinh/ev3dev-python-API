import os
import subprocess
print("This script is written for python3 or higher")
#A diagnostic script for file access
#requirres python§ or higher.

class diagnostic():
    def __init__(self, port):
        #list all motors and reads their address (port name) and compare it with 'port'
	#NOTE: I know, its not beautiful code there, but i have no idea, why i can't read the file 'address' and compare it with 'port' directly!
	#If I understand my script correctly, it founds a '\n' in the file that stores the port name
	#But its seems to be not correct!
	#if address == port:
	#	self.port = port
	#	self.N = item
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            rpn.close()
            if address.find(port) > -2:
                #if the port name can be found in address, then execute the code below
                self.N = item
        #have all datas, lets beginn test!
        points = 0        
        print("check, if '/sys/class/tacho-motor/" + self.N + "' exists")
        if os.path.exists("/sys/class/tacho-motor/" + self.N):
            print("  yes, it exists")
        else:
            print("  no, it doesn't exist. Please check the wire of the connected port and check, if you typed the port name correctly")
            print("  You has given me as port:" + port)
            return 1
        for item in os.listdir("/sys/class/tacho-motor/" + self.N):
            print("checking, if you have the following rights for /sys/class/tacho-motor/" + self.N + "/" + item)
            if os.path.isfile("/sys/class/tacho-motor/" + self.N + "/" + item):
                try:
                    s = open("/sys/class/tacho-motor/" + self.N + "/" + item, "r")
                    print("  read access...yes")
                    s.close()
                    points += 1
                except:
                    print("  read access...no")
                try:
                    sf = open("/sys/class/tacho-motor/" + self.N + "/" + item, "w")
                    print("  write access...yes")
                    sf.close()
                    points += 1
                except:
                    print("  write access...no")
                if points == 1:
                    print("Summary: You have read access, but not write access for file /sys/class/tacho-motor/" + self.N + "/" + item)
                elif points == 2:
                    print("Summary: You have read and write access for file /sys/class/tacho-motor/" + self.N + "/" + item)
                else:
                    print("Summary: You haven't read and write access for file /sys/class/tacho-motor/" + self.N + "/" + item)
                print("trying to make the problem an end")
                #this three terminal commands below should make the problem an end
                try:
                    subprocess.run(["sudo", "chown", "root:root", "/sys/class/tacho-motor/"+ self.N + "/command"])
                    subprocess.run(["sudo", "chown", "u+rw", "/sys/class/tacho-motor/"+ self.N + "/command"])
                    subprocess.run(["sudo", "chown", "g+rw", "/sys/class/tacho-motor/"+ self.N + "/command"])
                except:
                    print("Execute the following commands with root privilegs:")
                    print("sudo chown root:root /sys/class/tacho-motor/" + self.N + "/command")
                    print("sudo chmod u+rw /sys/class/tacho-motor/" + self.N + "/command")
                    print("sudo chmod g+rw /sys/class/tacho-motor/" + self.N + "/command")
                points = 0
