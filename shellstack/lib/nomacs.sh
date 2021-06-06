function easy_install_nomacs {
	echo "Will now install nomacs"
	sleep 3
	sudo add-apt-repository ppa:nomacs/stable
sudo apt-get update
sudo apt-get install nomacs
	echo "nomacs has been installed"
	sleep 3
}