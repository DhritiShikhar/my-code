#!/usr/bin/python3

#start() function is used to start a thread.

import time
from threading import Thread

def sleeper(i):
  print ("\nThread %d sleeps for 5 seconds" %(i))
  time.sleep(5)
  print ("\nThread %d woke up" %(i))

for i in range(10):
  t = Thread(target=sleeper, args=(i,))
  t.start()
