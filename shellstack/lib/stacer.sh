function easy_install_stacer {
	echo "Will now install stacer"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:oguzhaninan/stacer
sudo apt-get update
sudo apt-get install stacer
	echo "stacer has been installed"
	sleep 3
}