#!/bin/sh
TIMES=0
while [ $TIMES -lt 2 ]
    do
        sleep 2
        TIMES=$((TIMES+1))
        echo "$TIMES"
    done
    echo "------------"
