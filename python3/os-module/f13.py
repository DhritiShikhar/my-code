#!/usr/bin/python3

#This script uses os module to start a new process

#exec function starts a new process, replacing teh current one 
#execvp searches for the program along standard path, passes arguments and runs it under current environment


import os, sys

program = "python"
arguments = ["f11.py"]

print (os.execvp(program, (program,) + tuple(arguments)))
print ("Goodbye") #This is never printed


