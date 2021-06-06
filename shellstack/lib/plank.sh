function easy_install_plank {
	echo "Will now install plank"
	sleep 3
	sudo add-apt-repository ppa:ricotz/docky
sudo apt-get update
sudo apt-get install plank
	echo "plank has been installed"
	sleep 3
}