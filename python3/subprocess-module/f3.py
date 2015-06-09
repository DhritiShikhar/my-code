#!/usr/bin/python3

#Ping program using subprocess

import subprocess

host = input("Enter a host to ping:\t")
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)
output = p1.communicate()[0]
print (output)
