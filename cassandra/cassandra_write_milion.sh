
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
 cassandra-stress write n=1000000 -rate threads=50 