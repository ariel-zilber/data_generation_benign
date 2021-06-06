function easy_install_conky-manager {
	echo "Will now install conky-manager"
	sleep 3
	sudo add-apt-repository ppa:teejee2008/ppa
sudo apt-get update
sudo apt-get install conky-manager
	echo "conky-manager has been installed"
	sleep 3
}