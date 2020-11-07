#!/bin/bash

for sg in $(jq '.sg | .[]' params.json); do
    for window in $(jq '.window | .[]' params.json); do
        for size in $(jq '.size | .[]' params.json); do
            python train.py $sg $window $size
        done
    done
done
