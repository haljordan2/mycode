#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')
#Creates a backup of a file.
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
#Creates a backup of the entire folder.
shutil.copytree('5g_research/', '5g_research_backup/')

