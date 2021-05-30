function easy_install_audacity {
	echo "Will now install audacity"
	sleep 3
	sudo add-apt-repository ppa:ubuntuhandbook1/audacity -y 
sudo apt-get update
sudo apt-get install -y  audacity
	echo "audacity has been installed"
	sleep 3
}