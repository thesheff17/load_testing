##### other info

#### golang

##### version1
golang has maps but maps have no order.  While maps seem very efficent for doing += 1 operations having no order does cause problems.  This is why you see a shell script in version1 that does the sort and head -n 10.  This seems very effiecent though.  I'm able to write the entire dataset to the file system, sort, and print the top 10 at the same speed at which version2 is running.

##### version2
version2 uses the same map concept.  Once the data structure is created I loop through it generating a struct that I can then sort.  This struct is then looped through 10 times to get the top 10 IP addresses.  This script runs almost in identical time as version1 which is interesting.  This script stores more in memory and less on the file system since we are not writing out the entire data set.  See version1 if you want the dataset written to the file system.

#### python
I thought calling python with multiprocessing would speed up reading and getting the IP adddresses of the system.  Unfortunately this generates allot more data and requires allot more RAM.  It kept crashing aws instances on me because the dataset it was generating was too much.  I then tested reader_single_logs.py setup where we keep track of things in a single python dictionary.  This was surprisingly around the same speed and requires allot less RAM.  All the scripts I write I try to make sure they run on the cheapest hardware as well.  A t2.nano server performance is almost identical from python to golang.  reader_logs.sh won't finish or will end up using all the CPU credits.


```
t2.nano
40GB EBS volume IOPS 120 / 3000	

./write_logs.sh
Python 3.6.8
generating ip list...
ip_list ready.
CPU count set to: 1
178.9678018093109

real	2m59.183s
user	2m40.356s
sys	0m10.674s

time ./reader_single_logs.py
number of unique IP addresses: 129032
191.99630188941956

real	3m12.222s
user	2m5.121s
sys	0m5.089s

time ./version1
script started...
893,"10.1.91.155"
891,"192.168.81.145"
891,"192.168.198.15"
891,"192.168.114.47"
890,"192.168.149.246"
890,"10.1.25.78"
888,"192.168.2.209"
888,"192.168.100.98"
887,"192.168.45.128"
886,"192.168.191.139"

Number of unique IP addresses:
129032
Number lines processed:
100010000

real	3m1.449s
user	1m52.736s
sys	0m6.800s

time ./version2
script started...
building struct for sort...
"10.1.91.155" : 893
"192.168.198.15" : 891
"192.168.114.47" : 891
"192.168.81.145" : 891
"10.1.25.78" : 890
"192.168.149.246" : 890
"192.168.100.98" : 888
"192.168.2.209" : 888
"192.168.45.128" : 887
"192.168.191.139" : 886
Number of unique IP addresses:
129032
Number lines processed:
100010000

real	3m2.120s
user	1m51.476s
sys	0m6.948s

```
