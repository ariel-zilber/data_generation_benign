""" This module is used to create simple installation scripts

"""

LIB_TEMPLATE = """function easy_install_%s {
	echo "%s"
	sleep 3
	%s
	echo "%s"
	sleep 3
}"""

LIB_RELATIVE_PATH = "shellstack/lib/"

RECIPES_TEMPLATE = """#!/bin/bash
source "$ROOT_PATH/recipes/basic"
source "$LIB_PATH/%s.sh"
function defaults_basic {
	#TODO: verify if vars are set and then use defautls our get 'em another way
	HOST_NAME="myhost"
	USER_NAME="myuser"
	USER_PASSWORD="mys3cr3t"
	USER_SSH_KEY="ssh-rsa paste here your ~/.ssh/id_rsa.pub"
}

function install_%s {
	# install_basic
   easy_install_%s
}"""

RECIPES_RELATIVE_PATH = "shellstack/recipes/"


def create_lib_file(package_name: str, install_command: str):
    """

    :param package_name:
    :param install_command:
    :return:
    """
    with open(LIB_RELATIVE_PATH + "/" + package_name + ".sh", "w") as f:
        f.write(LIB_TEMPLATE % (package_name, "Will now install " + package_name,
                                install_command, package_name + " has been installed")
                )


def create_recipe(recipe_name):
    with open(RECIPES_RELATIVE_PATH + "/" + recipe_name, 'w') as f:
        f.write(RECIPES_TEMPLATE % (recipe_name, recipe_name, recipe_name))


def install_basic(package_name: str, install_command: str):
    create_lib_file(package_name, install_command)
    create_recipe(package_name)


def generate_all():
    "https://linuxhint.com/100_best_ubuntu_apps/"

    # python
    install_basic("python3_9", "sudo apt install python3.9 -y")

    # steam
    install_basic("steam",
                  "sudo add-apt-repository multiverse\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install steam")

    # vlc media
    install_basic("vlc_media",
                  "sudo add-apt-repository ppa:videolan/master-daily\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install vlc qtwayland5")

    # vlc media
    install_basic("atom_text_editor",
                  "sudo add-apt-repository ppa:webupd8team/atom\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install atom")

    # gimp
    install_basic("gimp", "sudo apt-get install gimp")

    # synaptic
    install_basic("synaptic", "sudo apt-get install synaptic")

    # Skype
    install_basic("skype",
                  "sudo snap install skype")

    # unity-tweak-tool
    install_basic("unity-tweak-tool",
                  "sudo apt-get install unity-tweak-tool")

    # ubuntu-cleaner
    install_basic("ubuntu-cleaner",
                  "sudo add-apt-repository ppa:gerardpuig/ppa\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install ubuntu-cleaner")

    # corebird
    install_basic("corebird", " sudo snap install corebird")

    # clementine
    install_basic("clementine",
                  "sudo add-apt-repository ppa:me-davidsansome/clementine\n"+
                  "sudo apt-get update\n"+
                  "sudo apt-get install clementine"
                  )

    # audacity
    install_basic("audacity",
                  "sudo add-apt-repository ppa:ubuntuhandbook1/audacity\n"+
                  "sudo apt-get update\n"+
                  "sudo apt-get install audacity"
                  )

    # vim
    install_basic("vim", "sudo apt-get install vim")

    # inkscape
    install_basic("inkscape",
                  "sudo add-apt-repository ppa:inkscape.dev/stable\n"+
                  "sudo apt-get update\n"+
                  "sudo apt-get install inkscape"
                  )

generate_all()