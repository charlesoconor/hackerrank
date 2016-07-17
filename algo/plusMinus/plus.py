#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-11 21:02 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

posative=0
negative=0
zero=0

for x in arr:
    if x > 0:
        posative += 1
    elif x < 0:
        negative += 1
    else :
        zero += 1

print ( posative + 0.0 ) / n
print ( negative + 0.0 ) / n
print ( zero + 0.0 ) / n

