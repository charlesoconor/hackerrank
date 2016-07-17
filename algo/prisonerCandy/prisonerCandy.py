#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-11 21:02 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

n = int(raw_input().strip())
for i in range(n):
    arr = map(int,raw_input().strip().split(' '))
    
    n = arr[0]
    m = arr[1]
    s = arr[2]
    
    rem = ( m - 1 ) % n
    idNum = ( rem + s ) % ( n )

    # deal with no indexing from 0 like a normal person
    if idNum == 0:
        idNum = n

    print idNum

    
