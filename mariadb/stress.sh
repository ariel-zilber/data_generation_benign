#!/bin/bash

wget https://github.com/arikzilWork/install_mariadb/archive/refs/heads/main.zip
unzip main.zip

cd install_mariadb
sudo chmod 777 *
./install_mariadb.sh


# STEP 3: wait
sleep 2m

mysqlap -a --iterations=100