
#!/bin/bash

# STEP 1: get install script
wget wget https://github.com/arikzilWork/install_cassandra/archive/refs/heads/main.zip
unzip main.zip

# STEP 2: run install script
cd install_cassandra-main/
sudo chmod 777 *
./install_cassandra.sh

# STEP 3: wait
sleep 2m

# STEP 4: run stress test
 cassandra-stress mixed ratio\(write=1,read=3\) n=100000 cl=ONE -pop dist=UNIFORM\(1..1000000\) -schema keyspace="keyspace1" -mode native cql3 -rate threads\>=16 threads\<=256 -log file=~/mixed_autorate_50r50w_1M.log 