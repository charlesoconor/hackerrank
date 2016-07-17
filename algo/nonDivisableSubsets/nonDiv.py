#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016-07-11 21:02 coconor <coconor@umich.edu>
#

__author__ = "coconor" 

import sys

n,k = map(int,raw_input().strip().split(' '))
arr = map(int,raw_input().strip().split(' '))

max_size_of_set = 0

remanders = [ x % k  for x in arr ] 
remanders_value = dict()

for elm in remanders :
    remanders_value[ elm ] = remanders_value.get(elm, 0) + 1

# need to deal values that are divisable by k
if 0 in remanders_value:
    max_size_of_set += 1
    del remanders_value[0]

# remove any ones 
for key, value in remanders_value.iteritems():
    if (key * 2) % k == 0 :
         remanders_value[key] = min(value, 1)
    
# print remanders_value

for key1, value1 in list(remanders_value.iteritems()):
    for key2, value2 in list(remanders_value.iteritems()):
        if ( key1 + key2 ) % k == 0  and key1 != key2: # make sure we don't remove the same key
            # print "key1: " + str(key1) + " key2: " + str(key2)
            # remove the one with less value
            try : 
                if value1 > value2 :
                    del remanders_value[key2]
                else :
                    del remanders_value[key1]
            except KeyError:
                # Key errors are annoying 
                pass

for key, value in remanders_value.iteritems():
    max_size_of_set += value
    
print remanders_value
print max_size_of_set

