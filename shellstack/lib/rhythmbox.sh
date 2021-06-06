function easy_install_rhythmbox {
	echo "Will now install rhythmbox"
	sleep 3
	sudo add-apt-repository ppa:fossfreedom/rhythmbox
sudo apt-get update
sudo apt-get install rhythmbox
	echo "rhythmbox has been installed"
	sleep 3
}