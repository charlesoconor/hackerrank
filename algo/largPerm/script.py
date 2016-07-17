#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016-04-19 15:14 coconor <coconor@umich.edu>
#

# __author__ = "coconor" 

import sys

# if we want useful debug info to be printed
debug=False
def greedy( infile ):
    constants = infile.readline().strip().split(" ")
    if len(constants) < 2 :
        print("Need two constants N and K")
        exit(1)
    
    N=int(constants[0])
    K=int(constants[1])
    
    
    digets = infile.readline().strip().split(" ")
    
    if debug : 
        print "N: " + str(N) 
        print "K: " + str(K) 
        print digets

    digets_map=dict();
    index=0
    for d in digets:
        digets_map[d]=index
        index+=1

    print digets_map.pop();
    
    i = 0
    while i < K and i < N:
        # import pdb; pdb.set_trace()
        max_value = int(digets[i])
        index = i
        for j in range(N - 1, i, -1):
            if int(digets[j]) > max_value:
                max_value = int(digets[j])
                index = j
        if index != i:
            digets[index]=digets[i]
            digets[i]=max_value
        else:
            K+=1

        i+=1

    
    for d in digets:
        sys.stdout.write(str(d) + " ")
    print

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        greedy(open(sys.argv[1]))
    else:
        greedy(sys.stdin)

