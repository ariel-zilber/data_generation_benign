function easy_install_mvp-test {
	echo "Will now install mvp-test"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:mc3man/mpv-tests
sudo apt-get update
sudo apt-get install -y mpv
	echo "mvp-test has been installed"
	sleep 3
}