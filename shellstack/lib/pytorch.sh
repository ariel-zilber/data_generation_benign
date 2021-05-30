#!/bin/bash

function install_anaconda {
  echo "Will now install anaconda"
	sleep 3
	sudo sudo apt-get update -y
	curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh
	source ~/.bashrc
	conda config --set auto_activate_base false
	echo "anaconda has been installed"
	sleep 3
}


function easy_install_pytorch {

  install_anaconda
  echo "Will now install pytorch"
	sleep 3
	conda install pytorch torchvision cpuonly -c pytorch -y
	echo "pytorch has been installed"
	sleep 3
}