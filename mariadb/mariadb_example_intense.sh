
#!/bin/bash
sleep 5m
apt install unzip

wget https://github.com/arikzilWork/install_mariadb/archive/refs/heads/main.zip main
unzip main.zip

cd lsmain/

sudo chmod 777 *
./install_mariadb.sh


# STEP 3: wait
sleep 2m
 mysqlslap 
 --delimiter=";" \
 --create="CREATE TABLE t (a int);INSERT INTO t VALUES (5)" \
 --query="SELECT * FROM t" \
 --concurrency=40 \
 --iterations=10000 
     