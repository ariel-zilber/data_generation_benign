function easy_install_shutter {
	echo "Will now install shutter"
	sleep 3
	sudo add-apt-repository -y ppa:shutter/ppa
sudo apt update
sudo apt install shutter
	echo "shutter has been installed"
	sleep 3
}