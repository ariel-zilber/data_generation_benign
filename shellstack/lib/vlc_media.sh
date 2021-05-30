function easy_install_vlc_media {
	echo "Will now install vlc_media"
	sleep 3
	sudo add-apt-repository ppa:videolan/master-daily -y 
sudo apt-get update
sudo apt-get install  -y vlc qtwayland5
	echo "vlc_media has been installed"
	sleep 3
}