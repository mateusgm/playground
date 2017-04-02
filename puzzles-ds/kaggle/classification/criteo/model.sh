#!/usr/bin/env bash

if [ $1 == 'train' ]; then
    cat sample.txt | ./preprocess.py | vw --loss_function logistic --link logistic -b 25 -P 1e5 --passes 13 -c -k -f vw.model
fi

if [ $1 == 'test' ]; then
    ./preprocess.py t | vw -t -i vw.model -p /dev/stdout | ./postprocess.py > predictions.csv
fi
