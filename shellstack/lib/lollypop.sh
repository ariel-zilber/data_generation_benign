function easy_install_lollypop {
	echo "Will now install lollypop"
	sleep 3
	sudo add-apt-repository ppa:gnumdk/lollypop
sudo apt-get update
sudo apt-get install lollypop
	echo "lollypop has been installed"
	sleep 3
}