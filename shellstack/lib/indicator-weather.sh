function easy_install_indicator-weather {
	echo "Will now install indicator-weather"
	sleep 3
	sudo add-apt-repository ppa:kasra-mp/ubuntu-indicator-weather
sudo apt update
sudo apt install indicator-weather
	echo "indicator-weather has been installed"
	sleep 3
}