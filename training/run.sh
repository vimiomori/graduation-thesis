#!/bin/bash

COUNT=1

for sg in $(jq '.sg | .[]' params.json); do
    for window in $(jq '.window | .[]' params.json); do
        for size in $(jq '.size | .[]' params.json); do
            echo "==========" ITERATION $COUNT "=========="
            python train.py $sg $window $size
            RESULT=$?
            if [ $RESULT -eq 0 ]; then
                COUNT++
                continue
            else
                exit 1
            fi
        done
    done
done
