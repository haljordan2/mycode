#!/usr/bin/env python3

hostname = input('Please enter your username: ') #hostname set to user input

if hostname == 'MTG' or hostname == 'mtg' or hostname == 'mTg' or hostname == 'MTg' or hostname == 'mTG' or hostname == 'MtG':
	print('Hostname matches expected config') #hostname match criteria
else:
	print('Hostname does not match expected config')

# Script exit
exit = 'Exiting the script.'
print(exit) 
