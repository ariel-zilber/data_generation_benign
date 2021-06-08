
#!/bin/bash

# STEP 1: Install Packages Necessary for Apache Cassandra
sudo apt install openjdk-8-jdk -y
sudo apt install apt-transport-https -y

# STEP 2: Add Apache Cassandra Repository and Import GPG Key
sudo sh -c 'echo "deb http://www.apache.org/dist/cassandra/debian 40x main" > /etc/apt/sources.list.d/cassandra.list'
wget -q -O - https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -

# STEP 3: Install Apache Cassandra
sudo apt update
sudo apt install cassandra -y

# STEP 4: reset session   
sleep 10s
# STEP 5: enable cassandra   

# STEP 6: reset session   

# STEP 7: check status   
nodetool status

# STEP 8: stress test
bash -c "cassandra-stress mixed ratio\(write=1,read=3\) n=100000 cl=ONE -pop dist=UNIFORM\(1..1000000\) -schema keyspace="keyspace1" -mode native cql3 -rate threads\>=16 threads\<=256 -log file=~/mixed_autorate_50r50w_1M.log";exec bash