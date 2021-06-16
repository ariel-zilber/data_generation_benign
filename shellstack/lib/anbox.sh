echo "Will now install anbox"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:morphis/anbox-support
sudo apt-get update
udo apt install anbox-modules-dkms
snap install --devmode -- beta anbox
	echo "anbox has been installed"
	sleep 3
