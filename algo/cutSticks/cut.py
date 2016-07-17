#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-14 16:11 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def greaterThan(a,b):
    return a > b

arr.sort(reverse=False)

last_elm = arr[0]
num_remove_this_round = 0
print n

for elm in arr :
    if elm == last_elm :
        num_remove_this_round += 1
    else :
        # print 'num to remove: ' + str(num_remove_this_round)
        n -= num_remove_this_round
        print n

        num_remove_this_round = 1
        last_elm = elm
    
