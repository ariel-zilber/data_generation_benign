function easy_install_inkscape {
	echo "Will now install inkscape"
	sleep 3
	sudo add-apt-repository ppa:inkscape.dev/stable -y 
sudo apt-get update
sudo apt-get install -y inkscape
	echo "inkscape has been installed"
	sleep 3
}