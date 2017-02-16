# -*- coding: utf-8 -*-
import sys

from process import process

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 3:
        process(args[1], args[2], args[3])
    elif len(args) < 3:
        print 'wtf'
    else:
        process(args[1], args[2])
