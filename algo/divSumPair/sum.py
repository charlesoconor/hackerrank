#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-13 20:27 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys
# import pdb


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

sum_num = 0

for i in range(n):

    for j in range(i + 1,n):

        if (a[i] + a[j]) % k == 0 :
            sum_num += 1
        else :
            pass 

print sum_num
        
