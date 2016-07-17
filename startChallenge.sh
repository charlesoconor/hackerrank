#!/usr/bin/env bash
#
# startChallenge.sh
# Copyright (C) 2016-07-17 16:29 coconor <coconor@umich.edu>
#
#

echo $1

if [ -z $1 ]; then
    echo "Need to give a file path"
    exit 1
fi

mkdir -p $1
cd $_
tmux new -s $_

