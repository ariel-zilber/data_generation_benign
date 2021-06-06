function easy_install_teamviewer {
	echo "Will now install teamviewer"
	sleep 3
	wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
sudo apt install ./teamviewer_amd64.deb -y
	echo "teamviewer has been installed"
	sleep 3
}