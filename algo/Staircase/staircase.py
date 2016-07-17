#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-11 21:10 coconor <coconor@umich.edu>
#

__author__ = "coconor" 


import sys

n = int(raw_input().strip())

for i in range(n):
   print ( ' ' * (n - i - 1) + '#' * (i+1))

