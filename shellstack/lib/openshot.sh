function easy_install_openshot {
	echo "Will now install openshot"
	sleep 3
	sudo add-apt-repository ppa:openshot.developers/ppa
sudo apt update
sudo apt install openshot-qt
	echo "openshot has been installed"
	sleep 3
}