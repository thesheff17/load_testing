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

# this script will generate dummy apache2 logs.  
# The below command will generate about 10GB of data
# ./generate.py --lines 10000 --files 10000 

import argparse
import os
from multiprocessing import Pool, cpu_count
from time import time
import random
import shutil

parser = argparse.ArgumentParser(description='generate logs')
parser.add_argument('--lines', type=int, help='number of lines')
parser.add_argument('--files', type=int, help='number of files')

# some of these variables I need in a global scope so they are here.
print ("generating ip list...")
ip_list = []
prefix = "192."
for a in range (1, 255):
    for b in range (1, 255):
       for c in range (1, 255):
            ip_list.append(prefix + str(a) + "." + str(b) + "." + str(c))
print ("ip_list ready.")

END = ' - - [09/Jan/2015:19:12:06 +0000] 808840 "GET http://google.com HTTP/1.1" 200 17 "-" "POKEMON"'
args = parser.parse_args()

def check_dir():
    path = './test'
    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        shutil.rmtree("./test")
        os.mkdir(path)

def get_cpu():
    num_of_cpu = cpu_count()
    if num_of_cpu < 3:
        print ("cpu process set to 2")
        return 2
    else:
        print ("cpu process set to " + str(num_of_cpu - 2))
        return num_of_cpu - 2

def get_file_list(file_num):
    file_list = []
    for each in range (0, file_num):
        file_list.append("file" + str(each) + ".txt")
    return file_list

# def that runs in parallel   
def generate_logs(file_name):
    f = open("./test/" + file_name, "w+")
    for each in range (0, args.lines):
        f.write(random.choice(ip_list) + END + "\n")
    f.close()
    
if __name__ == "__main__":

    check_dir()
    args = parser.parse_args()
    file_list = get_file_list(args.files)
    num_of_cpu = get_cpu()
    
    start_time = time()
    with Pool(num_of_cpu) as p:
      p.map(generate_logs, file_list)
    end_time = time()
    seconds_elapsed = end_time - start_time
    print (seconds_elapsed)
