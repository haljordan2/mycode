#!/usr/bin/env python3
#The fake list:
my_list = [ "192.168.0.5", 5060, "UP" ]
#Popping the first time found in the Zero position of the list.
print("The first item in the list (IP): " + my_list[0] )
#Popping the 2nd item in the list as a string function.
print("The second item in the list (port): " + str(my_list[1]) )
#Up or down.
print("The last item in the list (state): " + my_list[2] )

#2nd list for exercise
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#Use the format command and calling the info from the new list to avoid formatting issues. 
print('When I {} into IP Addresses {} or {} I am unable to ping ports {}, {}, or {}.'.format(str(new_list[5]), new_list[3], new_list[4], new_list[0], str(new_list[1]), new_list[2]))
#Attempt to use Print without format. Unable to remove spaces added by Python3 at the punctuation at the end of the statement. 
print("When I" , str(new_list[5]), "into IP Addresses", new_list[3], "or", new_list[4], "I am unable to ping ports", str(new_list[0]) + ",", new_list[1] + ",", str(new_list[2]) + ".")