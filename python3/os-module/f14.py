#!/usr/bin/python3

#Using os module to run another program 

#Fork: makes a copy of current process
#wait: waits for child process to finish

import os, sys

def run(program, *args):
  pid = os.fork()
  if not pid: #we are in the new process
    os.execvp(program, (program,) + args)
  return os.wait()[0]

run("python", "f11.py")
print ("goodbye")
