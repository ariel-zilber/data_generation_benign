function easy_install_clementine {
	echo "Will now install clementine"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:me-davidsansome/clementine -y 
sudo apt-get update
sudo apt-get install  -y clementine
	echo "clementine has been installed"
	sleep 3
}