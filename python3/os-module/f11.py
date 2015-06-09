#!/usr/bin/python3

#Use of os module to change a file's priviledges and timestamps

import os, stat, time

infile = "Python-Logo.jpg"
outfile = "out.jpg"

fi = open(infile, "rb")
fo = open(outfile, "wb")

while 1:
  s = fi.read(10000)
  if not s:
    break
  fo.write(s)

fi.close()
fo.close()

st = os.stat(infile)
os.chmod(outfile, stat.S_IMODE(st[stat.ST_MODE]))
os.utime(outfile, (st[stat.ST_ATIME], st[stat.ST_MTIME]))

print ("original", "=>")
print ("Mode: ", oct(stat.S_IMODE(st[stat.ST_MODE])))
print ("atime: ", time.ctime(st[stat.ST_ATIME]))
print ("mtime: ", time.ctime(st[stat.ST_MTIME]))

print ("copy", "=>")
st = os.stat(outfile)
print ("Mode: ", oct(stat.S_IMODE(st[stat.ST_MODE])))
print ("atime: ", time.ctime(st[stat.ST_ATIME]))
print ("mtime: ", time.ctime(st[stat.ST_MTIME]))
