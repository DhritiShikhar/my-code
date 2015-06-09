#!/usr/bin/python3

import os

command = " "

while (command != "exit"):
  command = input("Command: ")
  handle = os.popen(command)
  line = " "
  while line:
    line = handle.read()
    print (line)
  handle.close()

print("\nBye. This is it")
