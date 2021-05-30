function easy_install_steam {
	echo "Will now install steam"
	sleep 3
	sudo add-apt-repository multiverse -y 
sudo apt-get update
sudo apt-get install  -y steam
	echo "steam has been installed"
	sleep 3
}