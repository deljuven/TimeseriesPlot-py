# -*- coding: utf-8 -*-
import sys

from preprocess import pre_process
from process import process

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4:
        print 'wtf'
    else:
        if args[1] == 'pre':
            if len(args) > 5:
                pre_process(args[2], args[3], args[4], int(args[5]))
            elif len(args) > 4:
                pre_process(args[2], args[3], args[4])
            else:
                pre_process(args[2], args[3])
        elif args[1] == 'proc':
            if len(args) == 4:
                process(args[2], args[3])
            elif len(args) == 5:
                process(args[2], args[3], float(args[4]))
            elif len(args) == 6:
                process(args[2], args[3], float(args[4]), int(args[5]))
            elif len(args) == 7:
                process(args[2], args[3], float(args[4]), int(args[5]), int(args[6]))
