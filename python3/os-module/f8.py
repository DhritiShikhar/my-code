#!/usr/bin/python3

import os

#os.makedirs is used to create multiple directory levels
os.makedirs("test/multiple/levels")

fp = open("test/multiple/levels/file", "w")
fp.write("hello")
fp.close()

#os.remove is used to remove a certain file
os.remove("test/multiple/levels/file")

#os.removedirs is used to remove all empty directories along the given path
os.removedirs("test/multiple/levels")

