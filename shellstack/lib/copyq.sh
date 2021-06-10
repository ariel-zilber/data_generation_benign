function easy_install_copyq {
	echo "Will now install copyq"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:hluk/copyq
sudo apt-get update
sudo apt-get install copyq
	echo "copyq has been installed"
	sleep 3
}