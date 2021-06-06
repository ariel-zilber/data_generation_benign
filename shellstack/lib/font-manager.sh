function easy_install_font-manager {
	echo "Will now install font-manager"
	sleep 3
	sudo add-apt-repository ppa:font-manager/staging
sudo apt-get updatesudo apt-get install font-manager
	echo "font-manager has been installed"
	sleep 3
}