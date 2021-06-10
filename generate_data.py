""" This module is used to create simple installation scripts

"""
import os

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
CASSANDRA_RELATIVE_PATH = "cassandra/"
CASSANDRA_BENCHMARK = """
#!/bin/bash

# STEP 1: get install script
wget wget https://github.com/arikzilWork/install_cassandra/archive/refs/heads/main.zip
unzip main.zip

# STEP 2: run install script
cd install_cassandra-main/
sudo chmod 777 *
./install_cassandra.sh

# STEP 3: run stress test
"""


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


def generate_all_manual():
    "https://linuxhint.com/100_best_ubuntu_apps/"

    # python
    install_basic("python3_9", "sudo apt install python3.9 -y")

    # steam
    install_basic("steam",
                  "sudo add-apt-repository multiverse -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install  -y steam")

    # vlc media
    install_basic("vlc_media",
                  "sudo add-apt-repository ppa:videolan/master-daily -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install  -y vlc qtwayland5")

    # vlc media
    install_basic("atom_text_editor",
                  "sudo add-apt-repository ppa:webupd8team/atom -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install  -y atom")

    # gimp
    install_basic("gimp", "sudo apt-get install  -y gimp")

    # synaptic
    install_basic("synaptic", "sudo apt-get install  -y synaptic")

    # Skype
    install_basic("skype",
                  "sudo snap install  -y skype")

    # unity-tweak-tool
    install_basic("unity-tweak-tool",
                  "sudo apt-get install  -y unity-tweak-tool")

    # ubuntu-cleaner
    install_basic("ubuntu-cleaner",
                  "sudo add-apt-repository ppa:gerardpuig/ppa -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install  -y ubuntu-cleaner")

    # corebird
    install_basic("corebird", " sudo snap install corebird")

    # clementine
    install_basic("clementine",
                  "sudo add-apt-repository ppa:me-davidsansome/clementine -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install  -y clementine"
                  )

    # audacity
    install_basic("audacity",
                  "sudo add-apt-repository ppa:ubuntuhandbook1/audacity -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install -y  audacity"
                  )

    # vim
    install_basic("vim", "sudo apt-get install -y  vim")

    # inkscape
    install_basic("inkscape",
                  "sudo add-apt-repository ppa:inkscape.dev/stable -y \n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install -y inkscape"
                  )

    install_basic("vim", " sudo apt-get install vim")
    install_basic("inkscape", "sudo add-apt-repository ppa:inkscape.dev/stable\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install inkscape")

    install_basic("shotcut", "snap install shotcut -- classic")

    install_basic("simplescreenrecorder", " sudo add-apt-repository ppa:marten-baert/simplescreenrecorder\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install simplescreenrecorder")

    install_basic("telegram-desktop", "sudo snap install telegram-desktop")

    install_basic("caffeine", "sudo add-apt-repository ppa:eugenesan/ppa\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install caffeine -y")

    install_basic("neofetch", "sudo add-apt-repository ppa:dawidd0811/neofetch\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get update install neofetch")

    install_basic("liferea", "sudo add-apt-repository ppa:ubuntuhandbook1/apps\n" +
                  "sudo apt-get update\n" +
                  " sudo apt-get install liferea")

    install_basic("pidgin", "sudo apt-get install pidgin")

    install_basic("nautilus-dropbox", " sudo apt-get install nautilus-dropbox")

    install_basic("terminator", "sudo apt-get install terminator")

    install_basic("thonny", "sudo apt-get install thonny")

    install_basic("font-manager",
                  "sudo add-apt-repository ppa:font-manager/staging\n" +
                  "sudo apt-get update" +
                  "sudo apt-get install font-manager")

    install_basic("atril", " sudo apt-get install atril")

    install_basic("notepadqq",
                  "sudo add-apt-repository ppa:notpadqq-team/notepadqq\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install notepadqq")

    install_basic("bitcoin-qt", "sudo add-apt-repository ppa:bitcoin/bitcoin\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install bitcoin-qt")

    install_basic("guake", "sudo apt-get install guake")

    install_basic("kdeconnect", "sudo add-apt-repository ppa:webupd8team/indicator-kedeconnect\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install kdeconnect indicator-kdeconnect")

    install_basic("copyq", "sudo add-apt-repository ppa:hluk/copyq\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install copyq")

    install_basic("tilix", "sudo add-apt-repository ppa:webupd8team/terminix\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install tilix")

    install_basic("anbox", "sudo add-apt-repository ppa:morphis/anbox-support\n" +
                  "sudo apt-get update\n" +
                  "udo apt install anbox-modules-dkms\n" +
                  "snap install --devmode -- beta anbox")

    install_basic("openshot", "sudo add-apt-repository ppa:openshot.developers/ppa\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install openshot -qt")
    install_basic("plank", "sudo add-apt-repository ppa:ricotz/docky\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install plank")

    install_basic("stacer", "sudo add-apt-repository ppa:oguzhaninan/stacer\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install stacer")

    install_basic("hiri", "sudo snap install hiri")

    install_basic("sublime-text", "sudo apt-get install sublime-text")

    install_basic("kontact", "sudo add-apt-repository ppa: qr-tools-developers/qr-tools-stable\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install qtqr\n")

    install_basic("kontact", "sudo apt-get install kontact\n")
    install_basic("xmind", "sudo snap install xmind")

    install_basic("nitroshare",
                  "sudo apt-add-repository ppa:george-edison55/nitroshare\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install nitroshare"
                  )

    install_basic("konversation", "sudo apt-get install konversation\n")

    install_basic("quiterss", "sudo apt-get install quiterss\n")

    install_basic("mvp-test",
                  "sudo add-apt-repository ppa:mc3man/mpv-tests\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install -y mpv")

    # plume-creator
    install_basic("plume-creator", "sudo apt-get install plume-creator\n")

    # nomacs
    install_basic("nomacs",
                  "sudo add-apt-repository ppa:nomacs/stable\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install nomacs")

    # Qmmp
    install_basic("Qmmp", " sudo add-apt-repository ppa:forkotov02/ppa\n"
                  + "sudo apt-get update\n" +
                  "sudo apt-get install qmmp qmmp-q4 qmmp-plugin-pack-qt4")

    # geary
    install_basic("geary", "sudo apt install geary\n")

    # geany
    install_basic("geany", "sudo apt-get install geany\n")

    # mumble-server
    install_basic("mumble-server", "sudo apt-get install mumble-server\n")

    # Deluge
    install_basic("Deluge", "sudo add-apt-repository ppa:deluge-team/ppa\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install deluge")

    install_basic("snapd", "sudo apt install snapd\n" +
                  "sudo snap install code --classic")

    install_basic("peek", "sudo add-apt-repository ppa:peek-developers/stable\n" +
                  "sudo apt update\n" +
                  "sudo apt install peek")

    install_basic("indicator-weather",
                  "sudo add-apt-repository ppa:kasra-mp/ubuntu-indicator-weather\n" +
                  "sudo apt update\n" +
                  "sudo apt install indicator-weather")

    install_basic("MOC",
                  "sudo apt-get install moc moc-ffmpeg-plugin")
    install_basic("conky-manager", "sudo add-apt-repository ppa:teejee2008/ppa\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install conky-manager")

    install_basic("gdebi", " sudo apt-get install gdebi")
    install_basic("libreoffice",
                  "sudo apt install snapd\n" +
                  "sudo snap install libreoffice"
                  )

    install_basic("digikam",
                  "sudo apt install snapd\n" +
                  "sudo snap install digikam --beta")

    install_basic("geary", "sudo add-apt-repository ppa:geary-team/releases\n" +
                  "sudo apt install geary")

    install_basic("tilix",
                  "sudo apt-get update -y\n" +
                  "sudo apt-get install -y tilix")

    install_basic("tilix",
                  "sudo apt-get update -y\n" +
                  "sudo apt-get install -y tilix")

    install_basic("neofetch",
                  "sudo apt install snapd\n" +
                  "sudo snap install neofetch --beta")

    install_basic("flatpak",
                  "sudo apt install flatpak\n" +
                  "flatpak install flathub de.haeckerfelix.Shortwave")

    install_basic("rambox",
                  " sudo apt install snapd\n" +
                  "sudo snap install rambox")

    install_basic("blender",
                  "sudo apt install snapd\n" +
                  "sudo snap install blender --classic")

    install_basic("krita", "sudo add-apt-repository ppa:kritalime/ppa\n" +
                  "sudo apt update\n" +
                  "sudo apt install krita")

    install_basic("openshot",
                  "sudo add-apt-repository ppa:openshot.developers/ppa\n" +
                  "sudo apt update\n" +
                  "sudo apt install openshot-qt")

    install_basic("flatpak",
                  "flatpak install --user https://flathub.org/repo/appstream/org.pitivi.Pitivi.flatpakref\n" +
                  "flatpak install --user http://flatpak.pitivi.org/pitivi.flatpakref\n" +
                  "flatpak run org.pitivi.Pitivi//stable")

    install_basic("rhythmbox",
                  "sudo add-apt-repository ppa:fossfreedom/rhythmbox\n"
                  "sudo apt-get update\n" +
                  "sudo apt-get install rhythmbox")

    install_basic("lollypop",
                  "sudo add-apt-repository ppa:gnumdk/lollypop\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install lollypop")

    install_basic("amarok", "sudo apt-get update\nsudo apt-get install amarok")
    install_basic("cmus", "sudo add-apt-repository ppa:jmuc/cmus\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install cmus")
    install_basic("calligra", "sudo apt-get install calligra")
    install_basic("shutter",
                  "sudo add-apt-repository -y ppa:shutter/ppa\n" +
                  "sudo apt update\n" +
                  "sudo apt install shutter")

    install_basic("kazam",
                  "sudo add-apt-repository ppa:kazam-team/unstable-series\n" +
                  "sudo apt update\n" +
                  "sudo apt install kazam python3-cairo python3-xlib")
    install_basic("gnome-screenshot", "sudo apt-get update\nsudo apt-get install gnome-screenshot")
    install_basic("recordmydesktop", "sudo apt-get update\nsudo apt-get install gtk-recordmydesktop")
    install_basic("gedit", "sudo apt-get update\nsudo apt-get install gedit")

    install_basic("handbrake", "sudo add-apt-repository ppa:stebbins/handbrake-releases\n" +
                  "sudo apt-get update\n" +
                  "apt-get install handbrake")

    install_basic("gedit", "sudo add-apt-repository -y ppa:teejee2008/timeshift\n" +
                  "sudo apt-get update\n" +
                  "sudo apt-get install timeshift")

    install_basic("spotify", "snap install spotify")

    install_basic("ktouch", "sudo snap install ktouch")
    install_basic("deja-dup", "sudo snap install deja-dup --classic")

    #
    install_basic("teamviewer",
                  "wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb\n" +
                  "sudo apt install ./teamviewer_amd64.deb -y")

    install_basic("laptop-mode-tools",
                  "sudo add-apt-repository ppa:ubuntuhandbook1/apps\n" +
                  "sudo apt update\n" +
                  "sudo apt install laptop-mode-tools")


def generate_all_snaped():
    os.system('sh utils/get_snap_list.sh')

    with open("utils/snap-list.txt", "r+") as f:
        lines = f.readlines()
        for line in lines:
            install_basic(line, "sudo snap install " + line)

            print(line)


def gen_cassandra_test(name_test, test_content):
    result = CASSANDRA_BENCHMARK +"nohup "+ test_content+" &"
    with open(CASSANDRA_RELATIVE_PATH + "/" + "cassandra_" + name_test + ".sh", 'w') as f:
        f.write(result)


#
def generate_cassandra_benchmark_test():
    """
    https://docs.datastax.com/en/dse/5.1/dse-admin/datastax_enterprise/tools/toolsCStress.html

    """
    gen_cassandra_test("write_milion", "cassandra-stress write n=1000000 -rate threads=50")
    gen_cassandra_test("read_1000", "cassandra-stress read n=200000 -rate threads=50")
    gen_cassandra_test("read_3m", "cassandra-stress read duration=3m -rate threads=50")
    gen_cassandra_test("read_200000_nowarmup", "cassandra-stress read n=200000 no-warmup -rate threads=50")
    gen_cassandra_test("mixed", "cassandra-stress mixed ratio\(write=1,read=3\) "
                                "n=100000 cl=ONE "
                                "-pop dist=UNIFORM\(1..1000000\)"
                                " -schema keyspace=\"keyspace1\" "
                                "-mode native cql3 "
                                "-rate threads\>=16 threads\<=256 "
                                "-log file=~/mixed_autorate_50r50w_1M.log")


generate_cassandra_benchmark_test()
