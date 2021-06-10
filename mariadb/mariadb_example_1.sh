
#!/bin/bash

wget https://github.com/arikzilWork/install_mariadb/archive/refs/heads/main.zip
unzip main.zip

cd install_mariadb
sudo chmod 777 *
./install_mariadb.sh


# STEP 3: wait
sleep 2m
 mysqlslap 
 --delimiter=";" 
 --create="CREATE TABLE t (a int);INSERT INTO t VALUES (5)"
 --query="SELECT * FROM t"
 --concurrency=40
 --iterations=100
     