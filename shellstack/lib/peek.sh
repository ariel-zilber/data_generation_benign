function easy_install_peek {
	echo "Will now install peek"
	sleep 3
	sudo add-apt-repository ppa:peek-developers/stable
sudo apt update
sudo apt install peek
	echo "peek has been installed"
	sleep 3
}