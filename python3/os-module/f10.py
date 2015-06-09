#!/usr/bin/python3

#working with os module to get information about a file

import os, time

file = "Python-Logo.jpg"

def dump(st):
  mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
  print ("Size: ", size, "bytes")
  print ("Owner: ", uid, gid)
  print ("Created: ", time.ctime(ctime))
  print ("Last accessed: ", time.ctime(atime))
  print ("Last modified: ", time.ctime(mtime))
  print ("mode: ", oct(mode))
  print ("inode/dev: ", ino, dev)
 
st = os.stat(file)

print ("Stat: ", file)

dump(st)

print ()

fp = open(file)

st = os.fstat(fp.fileno())

print ("fstat: ", file)
dump(st) 
