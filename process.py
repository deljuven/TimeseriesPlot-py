# -*- coding: utf-8 -*-
import re
from datetime import datetime
from operator import itemgetter

MIN_TIME = datetime.strptime('1998-04-30 21:30:17', '%Y-%m-%d %H:%M:%S')
MAX_TIME = datetime.strptime('1998-7-26 21:59:55', '%Y-%m-%d %H:%M:%S')
BUFF_COUNT = 10000


def process(in_file, out_file=None, interval=0):
    result = {}
    result = read_from_file(in_file, result, interval * 60)
    ordered = sorted(result.items(), key=itemgetter(0))
    hint_order = sorted(result.items(), key=itemgetter(1), reverse=True)
    output(out_file, ordered, hint_order)


def read_from_file(file_, dict_, interval):
    begin = datetime.now()
    with open(file_, 'r') as in_file, open('./proc.log', 'w') as log:
        index = 0
        for line in in_file:
            index += 1
            print "line no %d" % index
            if interval == 0:
                key = data_process(line)
            else:
                key = data_process(line) / interval
            val = dict_.get(key)
            if val:
                val += 1
            else:
                val = 1
            dict_[key] = val
        duration = (datetime.now() - begin).total_seconds()
        log.write("read and parse cost seconds %s" % duration)
    print (datetime.now() - begin).total_seconds()
    return dict_


def parse_time(time_str):
    to_parse = time_str.split(' ')[0]
    delta = datetime.strptime(to_parse, '%d/%b/%Y:%H:%M:%S') - MIN_TIME
    return int(delta.total_seconds())


def data_process(line):
    regular = re.compile(r'\[(\S+)\s(\S+)\]')
    data = re.search(regular, line)
    return parse_time(data.group(1))


def output(out_file, statistics, hint_statics):
    hint_file = out_file + ".hint"
    with open(out_file, 'w') as fp, open(hint_file, 'w') as hfp:
        pt_count = 0
        ht_count = 0
        pt_buff = ""
        ht_buff = ""
        for point in statistics:
            pt_buff += "%s %s\n" % (point[0], point[1])
            if pt_count == BUFF_COUNT:
                fp.write(pt_buff)
                fp.flush()
                pt_count = 0
                pt_buff = ""
            pt_count += 1
        for hint in hint_statics:
            ht_buff += "%s %s\n" % (hint[0], hint[1])
            if ht_count == BUFF_COUNT:
                hfp.write(ht_buff)
                hfp.flush()
                ht_count = 0
                ht_buff = ""
            ht_count += 1
        if len(pt_buff) > 0:
            fp.write(pt_buff)
            fp.flush()
        if len(ht_buff) > 0:
            hfp.write(ht_buff)
            hfp.flush()
