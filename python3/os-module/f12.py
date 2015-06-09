#!/usr/bin/python3

#This script uses the os module to run an OS command

#os.system() runs a new command under current process and waits for it to finish

import os

if os.name == "nt":
  command = "dir"
else:
  command = "ls -l"

os.system(command)
