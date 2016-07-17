#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-13 20:58 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]

h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

arr = [h1, h2, h3]

def sum(arr):
    sum_cur = 0
    for el in arr:
        sum_cur += el

    return sum_cur

sums = [sum(h1),sum(h2),sum(h3)]

def allEqual( arr ):
    # is commented for this code for speed but should be in there
    # if len(arr) <= 0 :
    #     return True

    compare_val = arr[0]
    for cur in arr:
        if compare_val != cur :
            return False

    return True

def max_finder(arr):
    max_index = -1
    max_val = -1

    min_val = sys.maxint

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
        if arr[i] < min_val:
            min_val = arr[i]

    return (max_val, max_index, min_val)

while True :
    max_val, max_index, min_val = max_finder(sums)

    if max_val == min_val or min_val == 0 :
        print min_val
        break

    # reduce the largest sum by the element we just popped off
    sums[max_index] -= arr[max_index][0]
    # remove the first index in the array
    del arr[max_index][0]
        

