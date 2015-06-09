#!/usr/bin/python3

import sys

save_stdout = sys.stdout

my_file = open("test", "w")

sys.stdout = my_file

print ("This line goes to my_file")

sys.stdout = save_stdout

my_file.close()
