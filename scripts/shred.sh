#!/bin/bash

BASE_DIR=$(cd $(dirname $0)/..; pwd)
INPUT_DIR=$BASE_DIR/data/img
OUTPUT_DIR=$BASE_DIR/data/shred
H_BINS="3 5 10 30 50 100"
V_BINS="1 2 4"

if [ -d $OUTPUT_DIR ]; then
    echo Remove $OUTPUT_DIR
    rm -rf $OUTPUR_DIR
fi
mkdir -p $OUTPUT_DIR

for f in `ls $INPUT_DIR`; do
    echo Process $f
    for h in $H_BINS; do
        for v in $V_BINS; do
            python scripts/shredder.py --rows $v --cols $h $INPUT_DIR/$f $OUTPUT_DIR/${f%.*}_${v}_${h}.pkl
        done
    done
done