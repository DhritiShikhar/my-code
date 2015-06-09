#!/usr/bin/python3

import sys

save_stderr = sys.stderr

my_file = open("errors_f6", "w")
sys.stderr = my_file

x = 10/0

sys.stderr = save_stderr

my_file.close()
