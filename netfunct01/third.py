#!/usr/bin/env python3

configfile = open('dictionary.dic','r')
configlist = configfile.readlines()
print(configlist)

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    round = 0
    while(True):
        round = round + 3

        for coffeetime in configlist:
            print('Handshaking. .. ... connecting with ' + coffeetime[0])
            print('This is ' + coffeetime[1])
            print('Attempting to send command --> ' + coffeetime[2])
        
        
        # we'll learn to write code that connects to devices here
    #    for mycmds in devicecmd[coffeetime]:
     #       print('Attempting to sending command --> ' + mycmds)
        print()
            # we'll learn to write code that sends cmds to device here

### Start our script
#work2do = configlist

print("Welcome to the network device command pusher") # welcome message

## get data set

print("\nData set found\n") # replace with function call that reads in data from file

## run 
#commandpush(work2do) # call function to push commands to devices