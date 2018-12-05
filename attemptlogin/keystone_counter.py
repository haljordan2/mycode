#!/usr/bin/env python3

loginfail = 0    #Login failure initializes at zero.
success = 0 #2nd variable for successful logins
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')  #Opens the file to parse and sets it to variable.
keystone_file_lines=keystone_file.readlines()  #creates a list with an entry for every line in the keystone file. 

for i in range(len(keystone_file_lines)):  #El Loopo!
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
        tline = keystone_file_lines[i] #Creates tline variable for the full line of text that includes the IP address. 
        temp, ipaddress = tline.split('from ')  #Splits the tline variable into 2 variables temp / ipaddress. Uses the word "from " as the point of split. 
        print('Failed login is coming from:', ipaddress)  #Prints the ipaddress with a quick snip in front. 
        
    elif "-] Authorization failed" in keystone_file_lines[i]:  #elif that looks for matches on -] Auth failures. 
        success += 1
print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(success))