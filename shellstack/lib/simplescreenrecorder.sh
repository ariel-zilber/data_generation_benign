function easy_install_simplescreenrecorder {
	echo "Will now install simplescreenrecorder"
	sleep 3
	 sudo add-apt-repository ppa:marten-baert/simplescreenrecorder
sudo apt-get update
sudo apt-get install simplescreenrecorder
	echo "simplescreenrecorder has been installed"
	sleep 3
}