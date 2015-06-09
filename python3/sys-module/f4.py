#!/usr/bin/python3

#This script illustrates usage of standard data streams for input and output

import sys

while True:
  print ("\n\nThis script is in Iteration!\n")
  try:
    number = input("\nEnter a number: \t")
  except EOFError:
    print ("\nBye\n")
    break
  else:
    number = int(number)
    if number == 0:
      print >> std.err, "\n0 has no inverse\n"
    else:
      print ("\nInverse of %d is:\t %f" % (number, 1.0/number))
