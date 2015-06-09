#!/usr/bin/python3

#os.mkdir and os.rmdir can handle only single directory levels

import os

os.mkdir("test")
os.rmdir("test")

#This will fail
#os.rmdir("hello")

