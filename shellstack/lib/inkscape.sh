function easy_install_inkscape {
	echo "Will now install inkscape"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt-get update
sudo apt-get install inkscape
	echo "inkscape has been installed"
	sleep 3
}