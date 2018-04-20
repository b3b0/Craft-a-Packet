import os
from scapy.all import *

###############
#DETECT OS#####
###############

youros= os.name
if youros == 'nt':
    clear = lambda: os.system('cls')
if youros == 'posix':
    clear = lambda: os.system('clear')
clear()

#############################
#MAIN FUNCTIONS##############
#############################

def mainloop():
    packet = IP(dst=destination,src=source)/TCP(dport=999,sport=1234)/"iamhaxor"
    send(packet)
    packet.show()
    print "Press any key to continue"
    raw_input()
    quitter()

def quitter():
    uncertain = 1
    while uncertain == 1:
        keep = raw_input("Do you want to run the test with these settings again?")
        if keep == 'y':
            uncertain = 0
            mainloop()
        if keep == 'n':
            uncertain = 0
            clear()
            exit()
        else:
            clear()
            print 'Choose "y" or "n"'

###########################################
#START HERE################################
###########################################

print '''
   ____ ____      _    _____ _____       _         ____   _    ____ _  _______ _____
  / ___|  _ \    / \  |  ___|_   _|     / \       |  _ \ / \  / ___| |/ / ____|_   _|
 | |   | |_) |  / _ \ | |_    | |_____ / _ \ _____| |_) / _ \| |   | ' /|  _|   | |
 | |___|  _ <  / ___ \|  _|   | |_____/ ___ \_____|  __/ ___ \ |___| . \| |___  | |
  \____|_| \_\/_/   \_\_|     |_|    /_/   \_\    |_| /_/   \_\____|_|\_\_____| |_|
'''
source = raw_input("SOURCE IP:")
destination = raw_input("DESTINATION IP:")
mainloop()
