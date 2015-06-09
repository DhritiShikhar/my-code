#!/usr/bin/python3

#This script shows access to the command line arguments

#sys.argv[] is a list which contains the command line arguments passed to the script. the first item in the list is the script name itself.

import sys

print (sys.argv)

i = 0

for i in range(len(sys.argv)):
  if i == 0:
    print ("Function name: %s" %(sys.argv[0]))
  else:
    print ("%d. argument: %s" %(i, sys.argv[i]))
