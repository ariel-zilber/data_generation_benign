function easy_install_krita {
	echo "Will now install krita"
	sleep 3
	sudo add-apt-repository ppa:kritalime/ppa
sudo apt update
sudo apt install krita
	echo "krita has been installed"
	sleep 3
}