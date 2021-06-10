#!/bin/bash
sysbench /usr/share/sysbench/oltp_read_only.lua \
--mysql-host=127.0.0.1 \
--mysql-port=3306 \
--mysql-user=root \
--mysql-password='pass' \
--mysql-db=dbname \
--db-driver=mysql \
--tables=10 \
--table-size=100000 \
--report-interval=10 \
--threads=10 \
--time=120 \
prepare