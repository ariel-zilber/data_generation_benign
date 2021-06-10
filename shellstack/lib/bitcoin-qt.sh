function easy_install_bitcoin-qt {
	echo "Will now install bitcoin-qt"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get install bitcoin-qt
	echo "bitcoin-qt has been installed"
	sleep 3
}