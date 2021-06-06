function easy_install_Deluge {
	echo "Will now install Deluge"
	sleep 3
	sudo add-apt-repository ppa:deluge-team/ppa
sudo apt-get update
sudo apt-get install deluge
	echo "Deluge has been installed"
	sleep 3
}