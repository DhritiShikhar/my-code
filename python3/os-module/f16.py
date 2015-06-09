#!/usr/bin/python3

#Using os module to run as daemon

import os, time

pid = os.fork()
if pid:
  os._exit(0) #kill original

print ("daemon started")
time.sleep(10)
print ("daemon terminated")
