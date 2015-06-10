#!/usr/bin/python3

#This script forks iteratively and quits when q is pressed.

import os

def child():
  print ("A new child: ", os.getpid())
  os._exit(0)

def parent():
  while True:
    newpid = os.fork()
    if newpid == 0:
      child()
    else:
      pids = (	os.getpid(), newpid)
      print ("Parent: %d\t Child %d" %(pids))
    if input() == 'q':
      break

parent()
