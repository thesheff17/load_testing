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
# ./reader.py

import os
from time import time
import glob
import sys
from collections import Counter


def check_dir():
    path = './test'
    if not os.path.isdir(path):
        print('you do not have a ./test directory. exiting...')
        sys.exit(1)


def generate_logs():
    ip_list = Counter()
    for each in glob.glob("./test/*"):
        with open(each) as fin:
            for line in fin:
                ip_list[line.split(" ")[0]] += 1
    print("number of unique IP addresses: " + str(len(ip_list)))

    # quick way to see what this script is producing
    # for now I will leave it commented out
    f = open("reader_single_output.txt", "w+")
    f.write(str(ip_list))
    f.close()

    return ip_list


if __name__ == "__main__":

    check_dir()
    start_time = time()
    generate_logs()
    end_time = time()
    seconds_elapsed = end_time - start_time
    print(seconds_elapsed)
