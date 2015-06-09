#!/usr/bin/python3

#f1.py works well only on Linux. This is a platform independent script

import os, platform

if platform.system() == "Windows":
  import msvcrt

def getch():
  if platform.system() == "Linux":
    os.system("bash -c \"read -n 1\"")
  else:
    msvcrt.getch()

print("\nType a key")
getch()
print("\nOkay")
  
