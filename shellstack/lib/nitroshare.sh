function easy_install_nitroshare {
	echo "Will now install nitroshare"
	sleep 3
	sudo apt-add-repository ppa:george-edison55/nitroshare
sudo apt-get update
sudo apt-get install nitroshare
	echo "nitroshare has been installed"
	sleep 3
}