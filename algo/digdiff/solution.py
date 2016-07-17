#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)


right = 0
left = 0

for i in range(n):
    right += a[i][i]
    index = n - 1 - i
    left += a[index][i]

print abs(right - left)
    
