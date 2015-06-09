#!/usr/bin/python3

#getch() waits for one character to be typed without a return

#Bash command "read -n 1" waits for a key to be typed

#os.system doesnot return result of called shell commands

import os

def getch():
  os.system("bash -c \"read -n 1\"")

getch()
