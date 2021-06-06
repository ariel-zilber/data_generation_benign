function easy_install_cmus {
	echo "Will now install cmus"
	sleep 3
	sudo add-apt-repository ppa:jmuc/cmus
sudo apt-get update
sudo apt-get install cmus
	echo "cmus has been installed"
	sleep 3
}