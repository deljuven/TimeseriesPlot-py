#!/bin/sh
if [ ! $1 ] ;then
    pypy app.py pre ./input/result.out ./output/all.out 1> ./log/pre_stat.log  2> ./log/pre_error.log
else
    pypy app.py pre ./input/result.out ./output/all_$2.out $2 1> ./log/pre_stat.log 2> ./log/pre_error.log
fi
