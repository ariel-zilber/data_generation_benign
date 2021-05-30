#!/bin/bash

# install dependencies
sudo apt-get install gcc -y
sudo apt-get install make -y
sudo apt-get install git -y

# get repository
git clone https://github.com/redis/redis.git

cd redis

# build
make distclean
make