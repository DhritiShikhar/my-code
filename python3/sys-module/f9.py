#!/usr/bin/python3

#Using the sys module to manipulate module search path

import sys

print ("Path has ", len(sys.path), "members")

sys.path.insert(0, "samples")
import sample

sys.path = []
import random
