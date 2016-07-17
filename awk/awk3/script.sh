#!/usr/bin/env bash
#
# script.sh
# Copyright (C) 2016-04-18 21:10 coconor <coconor@umich.edu>
#
#


awk '{
    if ((getline tmp) > 0) {
        print $0";"tmp;
    }
    else {
        print $0;
    }
}' "$1"
