# load_testing

## Description 
This is a collection of scripts that will simulate logs being generated 
by a web server.  

I want to be able to do the following things:
- read logs off file system as fast as possible
- generate a data structure that counts the number IP adrress hits
- prints or writes the top 10 IP addresses to a screen or file 

Please make pull request if you see faster ways of doing this.  

There is some helper scripts:
```
./load_test/python/write_logs.sh
```
This script will write out about 10GB of log files into the test directory.
This script will require python3.

See otherinfo.md

#### test box
Current Date: Oct 31 2019
4790K 
ubuntu 18.04
4.15.0-64-generic
16GB RAM
Samsung SSD 850 EVO 500GB

golang:
```
time ./version1
script started...
901,"192.168.181.152"
895,"10.1.145.170"
887,"192.168.34.112"
885,"192.168.85.202"
884,"10.1.114.137"
883,"192.168.13.204"
883,"192.168.112.213"
883,"10.1.163.23"
881,"192.168.84.127"
881,"192.168.34.103"

Number of unique IP addresses:
129032
Number lines processed:
100010000

real	0m55.503s
user	1m8.898s
sys	0m2.639s 

time ./version2
script started...
building struct for sort...
"192.168.181.152" : 901
"10.1.145.170" : 895
"192.168.34.112" : 887
"192.168.85.202" : 885
"10.1.114.137" : 884
"192.168.112.213" : 883
"10.1.163.23" : 883
"192.168.13.204" : 883
"192.168.34.103" : 881
"192.168.84.127" : 881
Number of unique IP addresses:
129032
Number lines processed:
100010000

real	0m54.786s
user	1m8.120s
sys	0m2.547s
```

python:
```
time ./reader_single_logs.py
number of unique IP addresses: 129032
81.50755906105042

real	1m21.587s
user	1m18.808s
sys	0m2.768s

time ./reader_logs.py
CPU count set to: 8
finished map function call...
33.06000876426697
Time took to combine dictionaries...
118.92307829856873
number of unique ip address: 129032

real	2m33.957s
user	5m27.475s
sys	0m18.256s

time ./reader_logs.py
CPU count set to: 8
finished map function call...
33.59377717971802
Time took to combine dictionaries...
112.61526894569397
number of unique ip address: 129032

real	2m28.187s
user	5m21.969s
sys	0m18.982s
```


