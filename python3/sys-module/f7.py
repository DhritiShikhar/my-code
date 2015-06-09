#!/usr/bin/python3

import sys

save_stderr = sys.stderr
my_file = ("errors_f7", "w")
sys.stderr = my_file

print >> sys.stderr, "Printing to the error_f7 file"

sys.stderr = save_stderr

my_file.close()
