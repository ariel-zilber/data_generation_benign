function easy_install_kdeconnect {
	echo "Will now install kdeconnect"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:webupd8team/indicator-kedeconnect
sudo apt-get update
sudo apt-get install kdeconnect indicator-kdeconnect
	echo "kdeconnect has been installed"
	sleep 3
}