function easy_install_gedit {
	echo "Will now install gedit"
	sleep 3
	sudo add-apt-repository -y ppa:teejee2008/timeshift
sudo apt-get update
sudo apt-get install timeshift
	echo "gedit has been installed"
	sleep 3
}