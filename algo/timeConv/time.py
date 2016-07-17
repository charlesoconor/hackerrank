#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-12 09:29 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

time = raw_input().strip()

first = time[:2]
middle = time[2:8]
end = time[8:]

if end == 'PM' :
    if int(first) != 12:
        first = int(first) + 12
elif int(first) == 12 :
    first = '00'

print str(first) + middle

