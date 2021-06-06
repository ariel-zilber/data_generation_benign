function easy_install_caffeine {
	echo "Will now install caffeine"
	sleep 3
	sudo add-apt-repository ppa:eugenesan/ppa
sudo apt-get update
sudo apt-get install caffeine -y
	echo "caffeine has been installed"
	sleep 3
}