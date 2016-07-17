#! /usr/bin/env python
#
# Copyright  2016-04-21 19:07 coconor <coconor@umich.edu>
#


__author__ = "coconor" 

import sys

data = sys.stdin.readlines()
output = ""
for leter in data[0]:
    output += str((int(leter) + 1)%10)

print(output)
