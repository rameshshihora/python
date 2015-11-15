#!/usr/bin/python
from  __future__ import print_function

# read the lines from the file

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("Something wrong ({})".format(e))
