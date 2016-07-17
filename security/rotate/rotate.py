#! /usr/bin/env python
#
# Copyright 2016-04-22 13:15 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

data = sys.stdin.readlines()
num = int(data[1].strip())
output = ""
for leter in data[0].strip():
    output += str((int(leter) + num)%10)

print(output)


