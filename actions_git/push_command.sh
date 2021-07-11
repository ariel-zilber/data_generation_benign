#!/bin/bash

# install git
sudo apt install git-all -y

# setup credentials
git config --global user.name "yosi cohen"
git config --global user.email "yonicohen187@gmail.com"



mkdir test
cd test

git init

git status

touch