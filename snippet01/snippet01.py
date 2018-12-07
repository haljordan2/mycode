#!/usr/bin/env python3

#Opening List.txt and using it to create configlist list. 
configfile = open('list.txt', 'r')
configlist = configfile.readlines()
#print(configlist) #commenting out

print("\n".join(configlist))
print('\t'.join(configlist))
