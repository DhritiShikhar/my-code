#!/usr/bin/python3

#using os module to change working directory

#os.cwd() returns the path of current working directory.

import os

cwd = os.getcwd()
print("Current Working Directory:\n %s" %(cwd))

os.chdir("dir1")
print("\nWe go to chile directory using os.chdir().\nNow Current Working Directory:\n %s" %(os.getcwd()))

os.chdir(os.pardir)
print("\nWe go to parent directory using os.pardir().\nNow Current Working Directory:\n %s" %(os.getcwd()))


