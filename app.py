# -*- coding: utf-8 -*-
import sys

from process import process, MIN_TIME, MAX_TIME

if __name__ == '__main__':
    print sys.argv
    process(sys.argv[1], sys.argv[2])
