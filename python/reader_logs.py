#!/usr/bin/env python3

# Copyright (c) Dan Sheffner Digital Imaging Software Soltuions, INC
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# This script will attempt to read multiple log files as fast as possible.
# ./reader_logs.py

import os
from multiprocessing import Pool, cpu_count
from time import time
import glob
from collections import Counter
from collections import ChainMap
import sys
import operator


def check_dir():
    path = './test'
    if not os.path.isdir(path):
        print('you do not have a ./test directory. exiting...')
        sys.exit(1)


def merge_defaultdicts(d, d1):
    for k, v in d1.items():
        if (k in d):
            d[k].update(d1[k])
        else:
            d[k] = d1[k]
    return d


# def that runs in parallel
def generate_logs(file_name):
    # print(file_name)
    ip_list = Counter()
    with open(file_name) as fin:
        for line in fin:
            ip_list[line.split(" ")[0]] += 1
    return ip_list


if __name__ == "__main__":

    check_dir()
    file_list = list(glob.glob('./test/*'))
    # print(file_list)

    print("CPU count set to: " + str(cpu_count()))
    start_time = time()
    # p = Process(target=generate_logs, args=('bob',))
    with Pool(cpu_count()) as p:
        output = p.map(generate_logs, file_list)
    end_time = time()
    seconds_elapsed = end_time - start_time

    print("finished map function call...")
    print(seconds_elapsed)

    start_time1 = time()
    res = ChainMap(*output)
    end_time1 = time()
    seconds_elapsed1 = end_time1 - start_time1

    print("Time took to combine dictionaries...") 
    print(seconds_elapsed1)

    # output the top 10 IP addresses in the log
    a1_sorted_keys = sorted(res, key=res.get, reverse=True)
    f = open("reader_output.txt", "w+")
    x = 1
    for r in a1_sorted_keys:
        f.write("key: " + r + " value: " + str(res[r]) + "\n")
        if x > 9:
            break
        else:
            x += 1
    f.close()

    num_of_unique_ip = str(len(res))
    print("number of unique ip address: " + num_of_unique_ip)
