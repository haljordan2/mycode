#!/usr/bin/env python3

# function to push commands
def devicereboot(ipaddress): # ipaddress==list 
    for teatime in ipaddress:
        print('Connecting to... ' + teatime)
        print('Rebooting now!')
        print()

ips2do = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

print("IP Address Action Begin!")

print("\nData set found\n") # replace with function call that reads in data from file

devicereboot(ips2do)