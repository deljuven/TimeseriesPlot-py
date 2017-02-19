#!/bin/sh
if [ ! $1 ] ;then
    pypy app.py proc ./input/py.out ./output/interval_5.out 1> ./log/proc_stat.log  2> ./log/proc_error.log
else
    pypy app.py proc ./input/py.out ./output/interval_$2.out $2 1> ./log/proc_stat.log 2> ./log/proc_error.log
fi
