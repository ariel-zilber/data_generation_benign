function easy_install_ {
	echo "Will now install "
	sleep 3
	sudo add-apt-repository ppa:oguzhaninan/stacer
sudo apt-get update
sudo apt-get install stacer
	echo " has been installed"
	sleep 3
}