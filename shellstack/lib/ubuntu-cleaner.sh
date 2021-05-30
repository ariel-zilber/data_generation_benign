function easy_install_ubuntu-cleaner {
	echo "Will now install ubuntu-cleaner"
	sleep 3
	sudo add-apt-repository ppa:gerardpuig/ppa -y 
sudo apt-get update
sudo apt-get install  -y ubuntu-cleaner
	echo "ubuntu-cleaner has been installed"
	sleep 3
}