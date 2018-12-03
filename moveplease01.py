#!/usr/bin/env python3
import shutil
import os
#Set Dir to MyCode
os.chdir('/home/student/mycode/')
#Moves Raynor file 
shutil.move('raynor.obj', 'ceph_storage/')
#Prompts for rename of file if it already exists. 
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

