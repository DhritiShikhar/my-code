#!/usr/bin/python3

#Using os module to exit current process

#os._exit() function terminates current process. Unlinke sys.exit(), it works even if caller happens to catch SystemExit exeception.

import os, sys

try:
  sys.exit(1)
except SystemExit as value:
  print ("Caught exit(%s)" % (value))

try:
  os._exit(2)
except SystemExit as value:
  print ("Caught exit(%s)" % (value))

print ("Bye!")
