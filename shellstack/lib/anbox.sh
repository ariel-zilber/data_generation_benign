function easy_install_anbox {
	echo "Will now install anbox"
	sleep 3
	sudo add-apt-repository ppa:morphis/anbox-support
sudo apt-get update
udo apt install anbox-modules-dkms
snap install --devmode -- beta anbox
	echo "anbox has been installed"
	sleep 3
}