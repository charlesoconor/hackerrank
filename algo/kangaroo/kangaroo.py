#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-14 15:29 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

num_steps = 0
output_string = "YES"

def test(x1, v1, x2, v2):
    x_diff = x1 - x2
    v_diff = v2 - v1
    return v_diff != 0 and x_diff % v_diff == 0

if x1 != x2 :
    # check if there will never be an intersetion
    if x1 > x2 and v1 > v2 or x1 < x2 and v1 < v2 :
        output_string = 'NO'
    elif test(max(x1,x2),min(v1,v2),min(x1,x2),max(v1,v2)):
        output_string = 'YES'
    else :
        output_string = 'NO'

print output_string
    


