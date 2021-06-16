
#!/bin/bash
sleep 5m
apt install unzip

wget https://github.com/arikzilWork/install_mariadb/archive/refs/heads/main.zip 
unzip main.zip

cd install_mariadb-main/

sudo chmod 777 *
./install_mariadb.sh

# 
sed -i '/default-character-set = utf8mb4/d' /etc/mysql/mariadb.conf.d/50-client.cnf
systemctl restart mariadb.service

# STEP 3: wait
sleep 2m


 mysqlslap  \
 --delimiter=";" \
 --create="CREATE TABLE t (a int);INSERT INTO t VALUES (5)" \
 --query="SELECT * FROM t" \
 --concurrency=40 \
 --iterations=100 
     