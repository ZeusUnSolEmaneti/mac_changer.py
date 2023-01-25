import subprocess as s
import time
import optparse
import os 

os.system("clear")

print("""

█▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀   █▀▄▀█ █▀▀█ █▀▀   █▀▀ █░░█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ █▀▀█
▀▀█ ░░█░░ █▄▄█ █▄▄▀ ░░█░░   █░▀░█ █▄▄█ █░░   █░░ █▀▀█ █▄▄█ █░░█ █░▀█ █▀▀ █▄▄▀
▀▀▀ ░░▀░░ ▀░░▀ ▀░▀▀ ░░▀░░   ▀░░░▀ ▀░░▀ ▀▀▀   ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀


""")
time.sleep(0.5)
parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="İnterface To Change")
parse_object.add_option("-m","--mac",dest="ether",help="New Mac Adress")

(user_inputs,arguments)=parse_object.parse_args()

user_interface = user_inputs.interface
user_mac=user_inputs.ether

#interface=""
#ether=""

s.call(["ifconfig",user_interface,"down"])
s.call(["ifconfig",user_interface,"hw","ether",user_mac])
s.call(["ifconfig",user_interface,"up"])
print("Ok Your Mac Change...")
print(f"New Mac: {user_mac}")
ifconfig=s.check_output(["ifconfig",user_interface])
print(ifconfig)



#while True:
#    stop=input("İf You Want To Stop(s): ")
#    if stop=="s":
#        s.call(["ifconfig",interface,"down"])
#        s.call(["ifconfig",interface,"hw","ether","6c:60:eb:5b:df:f6"])
#        s.call(["ifconfig",interface,"up"])
#        break

