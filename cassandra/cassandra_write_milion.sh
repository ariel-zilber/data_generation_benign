
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
sleep 120s
# STEP 5: enable cassandra   

# STEP 6: reset session   

# STEP 7: check status   
nodetool status

# STEP 8: stress test
nohup cassandra-stress write n=1000000 -rate threads=50 &