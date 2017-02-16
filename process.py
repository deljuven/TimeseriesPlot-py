# -*- coding: utf-8 -*-
import re
from datetime import datetime
from operator import itemgetter

MIN_TIME = datetime.strptime('1998-04-30 21:30:17', '%Y-%m-%d %H:%M:%S')
MAX_TIME = datetime.strptime('1998-7-26 21:59:55', '%Y-%m-%d %H:%M:%S')


def process(in_file, out_file=None):
    result = {}
    result = read_from_file(in_file, result)
    ordered = sorted(result.items(), key=itemgetter(0))
    output(out_file, ordered)


def read_from_file(file_, dict_):
    with open(file_, 'r') as in_file:
        for line in in_file:
            key = data_process(line)
            val = dict_.get(key)
            if val:
                val += 1
            else:
                val = 1
            dict_[key] = val
    return dict_


def parse_time(time_str):
    to_parse = time_str.split(' ')[0]
    delta = datetime.strptime(to_parse, '%d/%b/%Y:%H:%M:%S') - MIN_TIME
    return int(delta.total_seconds())


def data_process(line):
    regular = re.compile(r'\[(\S+)\s(\S+)\]')
    data = re.search(regular, line)
    return parse_time(data.group(1))


def output(out_file, statistics):
    with open(out_file, 'w') as fp:
        for point in statistics:
            fp.write("%s %s\n" % (point[0], point[1]))
