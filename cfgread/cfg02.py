#!/usr/bin/env python3

filename = input('Please enter the name of the file: ')
## create file object in "r"ead mode
configfile = open(filename, 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## Always close your file
configfile.close()
print(len(configlist))