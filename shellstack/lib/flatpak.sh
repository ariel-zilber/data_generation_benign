function easy_install_flatpak {
	echo "Will now install flatpak"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	flatpak install --user https://flathub.org/repo/appstream/org.pitivi.Pitivi.flatpakref
flatpak install --user http://flatpak.pitivi.org/pitivi.flatpakref
flatpak run org.pitivi.Pitivi//stable
	echo "flatpak has been installed"
	sleep 3
}