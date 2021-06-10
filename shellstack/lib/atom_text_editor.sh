function easy_install_atom_text_editor {
	echo "Will now install atom_text_editor"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	sudo add-apt-repository ppa:webupd8team/atom -y 
sudo apt-get update
sudo apt-get install  -y atom
	echo "atom_text_editor has been installed"
	sleep 3
}