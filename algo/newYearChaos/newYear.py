#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-14 16:28 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

num_swaps = 0

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    toChaotic = False

    total_bibes = 0 
    # check if its chaotic 
    print q 
    for i in range(len(q)) :
        need_bribes = q[i] - 1 - i 
        print 'needed bribes ' + str(need_bribes)
        if need_bribes > 2 :
            toChaotic = True
            break
        else : 
            total_bibes += max(need_bribes, 0)

    if not toChaotic :
        print total_bibes 
    else : 
        print "Too chaotic"
