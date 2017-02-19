# -*- coding: utf-8 -*-
from datetime import datetime
from operator import itemgetter

BUFF_COUNT = 1000


def process(in_file, out_file=None, start=0, interval=5):
    result = {}
    result = read_from_file(in_file, result, start * 1440 / interval, interval * 60)
    ordered = sorted(result.items(), key=itemgetter(0))
    output(out_file, ordered)


def read_from_file(file_, dict_, start, interval):
    begin = datetime.now()
    with open(file_, 'r') as in_file, open('./log/process.log', 'w') as log:
        index = 0
        for line in in_file:
            index += 1
            point = parse_line(line)
            if start > point[0]:
                continue
            key = point[0] / interval
            val = dict_.get(key)
            if val:
                val += point[1]
            else:
                val = 1
            dict_[key] = val
        duration = (datetime.now() - begin).total_seconds()
        log.write("read and parse cost seconds %s" % duration)
    print (datetime.now() - begin).total_seconds()
    return dict_


def output(out_file, statistics):
    if not out_file:
        out_file = './interval_5.out'
    with open(out_file, 'w') as fp:
        pt_count = 0
        pt_buff = ""
        for point in statistics:
            pt_buff += "%s %s\n" % (point[0], point[1])
            if pt_count == BUFF_COUNT:
                fp.write(pt_buff)
                fp.flush()
                pt_count = 0
                pt_buff = ""
            pt_count += 1
        if len(pt_buff) > 0:
            fp.write(pt_buff)
            fp.flush()


def parse_line(line):
    return map(int, tuple(line.split(" ")))
