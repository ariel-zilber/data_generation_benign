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
	install_basic
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
        f.write(RECIPES_TEMPLATE % (recipe_name,recipe_name, recipe_name))


create_lib_file("python3_9", "sudo apt install python3.9 -y")
create_recipe("python3_9")