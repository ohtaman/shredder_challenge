#!/bin/bash

BASE_DIR=$(cd $(dirname $0)/..; pwd)
INPUT_DIR=$BASE_DIR/data/img
OUTPUT_DIR=$BASE_DIR/data/shred
H_BINS="5 10 30 50 100"
V_BINS="1 2 4"


for f in `ls $INPUT_DIR`; do
    echo Process $f
    for v in $H_BINS; do
        for h in $V_BINS; do
            python scripts/shredder.py --rows $v --cols $h $INPUT_DIR/$f $OUTPUT_DIR/${f%.*}_${v}_${h}.pkl
        done
    done
done