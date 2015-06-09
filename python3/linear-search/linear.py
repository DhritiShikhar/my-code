#!/usr/bin/python3

import sys

print ("The numbers are: \n")

for i in range(len(sys.argv)):
  if i != 0:
    print (sys.argv[i])

key = input("Enter the search number: ")

for i in range(len(sys.argv)):
  if i != 0:
    if key == sys.argv[i]:
      print ("The number is present at %d location" %(i))
 
