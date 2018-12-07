#!/usr/bin/env python3

print('This program will reserve a block of 10 ip addresses.')
ipaddy = input('Please enter a valid ip address: ')

#print(ipaddy)

def format(p):
    old_p = p
    new_p = p.split(".")
    #print(new_p)
    new_p_end = (int(new_p[3]) + 10)
    #print(new_p_end)
    print()
    if (new_p_end > 255):
        print('The IP address you entered is NOT valid.')
                
    else:
        print('The ip address you entered is valid.') 
        print('The starting IP address is: ' + old_p)
        print('The ending IP address for this IP range is: ' + new_p[0] + '.' + new_p[1] + '.' + new_p[2] + '.' + str(new_p_end))  
 
    print()
  
format(ipaddy)