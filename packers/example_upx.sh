#!/bin/bash
sudo apt-get install
wget https://github.com/upx/upx/releases/download/v3.96/upx-3.96-amd64_linux.tar.xz
tar -xvf upx-3.96-amd64_linux.tar.xz

upx-3.96-amd64_linux/upx
wget https://github.com/JonathanSalwan/binary-samples/archive/refs/heads/master.zip
tar -xvf master.zip



upx-3.96-amd64_linux/upx master/binary-samples-master/elf-Linux-x86-bash
upx-3.96-amd64_linux/upx master/binary-samples-master/elf-Linux-ARM64-bash
upx-3.96-amd64_linux/upx master/binary-samples-master/elf-Linux-ARMv7-ls

#wget https://github.com/arikzilWork/install_mariadb/archive/refs/heads/main.zip
#unzip main.zip


