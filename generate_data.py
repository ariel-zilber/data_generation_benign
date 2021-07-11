""" This module is used to create simple installation scripts

"""
import itertools
import os
from itertools import combinations

LIB_TEMPLATE = """echo "%s"
	sudo apt-get update
	sleep 2m
	#
	sleep 3
	%s
	echo "%s"
	sleep 3
"""

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
MARIADB_RELATIVE_PATH = "mariadb/"
MARIADB_BENCHMARK = """
#!/bin/bash
sleep 5m
apt install unzip

wget https://github.com/arikzilWork/install_mariadb/archive/refs/heads/main.zip 
unzip main.zip

cd install_mariadb-main/

sudo chmod 777 *
./install_mariadb.sh

# 
sed -i '/default-character-set = utf8mb4/d' /etc/mysql/mariadb.conf.d/50-client.cnf
systemctl restart mariadb.service

# STEP 3: wait
sleep 2m


"""

CASSANDRA_BENCHMARK = """
#!/bin/bash
sleep 5m
apt install unzip

# STEP 1: get install script
wget wget https://github.com/arikzilWork/install_cassandra/archive/refs/heads/main.zip
unzip main.zip

# STEP 2: run install script
cd install_cassandra-main/
sudo chmod 777 *
./install_cassandra.sh

# STEP 3: wait
sleep 2m

# STEP 4: run stress test
"""

###git related #######################################################################################################
GIT_CONFIG = """#!/bin/bash

# install git
sudo apt install git-all -y

# setup credentials
git config --global user.name "yosi cohen"
git config --global user.email "yonicohen187@gmail.com"
"""

#
GIT_SELECT_RAND_PROJECT = """
# select random project from top 100
allProjects=("https://github.com/freeCodeCamp/freeCodeCamp" "https://github.com/996icu/996.ICU" "https://github.com/EbookFoundation/free-programming-books" "https://github.com/vuejs/vue" "https://github.com/jwasham/coding-interview-university" "https://github.com/sindresorhus/awesome" "https://github.com/kamranahmedse/developer-roadmap" "https://github.com/tensorflow/tensorflow" "https://github.com/twbs/bootstrap" "https://github.com/getify/You-Dont-Know-JS" "https://github.com/public-apis/public-apis" "https://github.com/donnemartin/system-design-primer" "https://github.com/ohmyzsh/ohmyzsh" "https://github.com/flutter/flutter" "https://github.com/github/gitignore" "https://github.com/microsoft/vscode" "https://github.com/torvalds/linux" "https://github.com/trekhleb/javascript-algorithms" "https://github.com/danistefanovic/build-your-own-x" "https://github.com/TheAlgorithms/Python" "https://github.com/airbnb/javascript" "https://github.com/Snailclimb/JavaGuide" "https://github.com/jackfrued/Python-100-Days" "https://github.com/d3/d3" "https://github.com/ytdl-org/youtube-dl" "https://github.com/facebook/react-native" "https://github.com/electron/electron" "https://github.com/jlevy/the-art-of-command-line" "https://github.com/ossu/computer-science" "https://github.com/axios/axios" "https://github.com/justjavac/free-programming-books-zh_CN" "https://github.com/nodejs/node" "https://github.com/kubernetes/kubernetes" "https://github.com/microsoft/terminal" "https://github.com/angular/angular" "https://github.com/microsoft/TypeScript" "https://github.com/mrdoob/three.js" "https://github.com/puppeteer/puppeteer" "https://github.com/animate-css/animate.css" "https://github.com/tensorflow/models" "https://github.com/vercel/next.js" "https://github.com/mui-org/material-ui" "https://github.com/PanJiaChen/vue-element-admin" "https://github.com/iluwatar/java-design-patterns" "https://github.com/goldbergyoni/nodebestpractices" "https://github.com/laravel/laravel" "https://github.com/FortAwesome/Font-Awesome" "https://github.com/avelino/awesome-go" "https://github.com/MisterBooo/LeetCodeAnimation" "https://github.com/storybookjs/storybook" "https://github.com/nvbn/thefuck" "https://github.com/moby/moby" "https://github.com/angular/angular.js" "https://github.com/gothinkster/realworld" "https://github.com/webpack/webpack" "https://github.com/django/django" "https://github.com/microsoft/PowerToys" "https://github.com/tonsky/FiraCode" "https://github.com/rust-lang/rust" "https://github.com/apple/swift" "https://github.com/reduxjs/redux" "https://github.com/spring-projects/spring-boot" "https://github.com/pallets/flask" "https://github.com/atom/atom" "https://github.com/elastic/elasticsearch" "https://github.com/bitcoin/bitcoin" "https://github.com/opencv/opencv" "https://github.com/yangshun/tech-interview-handbook" "https://github.com/doocs/advanced-java" "https://github.com/netdata/netdata" "https://github.com/typicode/json-server" "https://github.com/jquery/jquery" "https://github.com/thedaviddias/Front-End-Checklist" "https://github.com/chartjs/Chart.js" "https://github.com/socketio/socket.io" "https://github.com/expressjs/express" "https://github.com/xingshaocheng/architect-awesome" "https://github.com/kdn251/interviews" "https://github.com/gohugoio/hugo" "https://github.com/adam-p/markdown-here" "https://github.com/tuvtran/project-based-learning" "https://github.com/keras-team/keras" "https://github.com/Genymobile/scrcpy" "https://github.com/httpie/httpie" "https://github.com/chrislgarry/Apollo-11" "https://github.com/h5bp/html5-boilerplate" "https://github.com/josephmisiti/awesome-machine-learning" "https://github.com/ElemeFE/element" "https://github.com/redis/redis" "https://github.com/lodash/lodash" "https://github.com/nvm-sh/nvm" "https://github.com/h5bp/Front-end-Developer-Interview-Questions" "https://github.com/gin-gonic/gin" "https://github.com/Semantic-Org/Semantic-UI" "https://github.com/pytorch/pytorch" "https://github.com/resume/resume.github.com" "https://github.com/ansible/ansible" "https://github.com/protocolbuffers/protobuf" "https://github.com/rails/rails" "https://github.com/sveltejs/svelte")
rand=$[$RANDOM % ${#allProjects[@]}]
project=${allProjects[$rand]}

git clone $project test
cd test
"""

GIT_ADD_REMOTE_REPOSITORY = """
git add *
git commit -m "first commit"

git remote add origin master ""
"""

#
GIT_CREATE_ENTER_FOLDER = """
# create and enter folder
mkdir test
cd test
"""

#
GIT_RESET_REMOTE = """
# remote all files from remote
git rm *
git commit -m "removed all"
git push origin master -f
"""

GIT_CREATE_SINGLE_FILE = """
# create a single file
echo "first file" >> README.md
git add README.md
git commit -m "added a single file"

"""

GIT_CREATE_MULTIPLE_FILES = """
# create multiple files

## init random amount of files

## add tje files to git

## commit the files
echo "first file" >> README.md
git add README.md
git commit -m "added multiple files"
"""

GIT_CREATE_FOLDER_SINGLE = """

# create a single folder
mkdir example_folder
touch example_folder/file.txt
git add *
git commit -m "added a single folder"
"""

GIT_CREATE_FOLDER_MULTIPLE = """

# create a multiple folders
declare -a arr=(1..10)

## now loop through the above array
for i in "${arr[@]}"
  mkdir example_folder
  touch example_folder/file${i}.txt
  git add *  
done 

git commit -m "added folders"

"""

GIT_REMOVE_ALL = """
# remove files git
git rm * -r
git add * 
git commit -m "removed all files"

"""

GIT_SWITCH_BRANCHES = """
# change to a new branch
git checkout -b 3d_printer
git add *
git commit -m "changed branch"
"""


def create_lib_file(package_name: str, install_command: str):
    """

    :param package_name:
    :param install_command:
    :return:
    """
    with open(LIB_RELATIVE_PATH + "/" + package_name + ".sh", "w") as f:
        f.write(LIB_TEMPLATE % ("Will now install " + package_name,
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
            #
            install_cmd = "sudo snap install " + line
            uninstall_cmd = install_cmd + "\n" + "sudo snap remove " + line

            install_basic("install_" + line, install_cmd)
            install_basic("install_uninstall_" + line, uninstall_cmd)

            print(line)


def gen_cassandra_test(name_test, test_content):
    result = CASSANDRA_BENCHMARK + " " + test_content + " "
    with open(CASSANDRA_RELATIVE_PATH + "/" + "cassandra_" + name_test + ".sh", 'w') as f:
        f.write(result)


def gen_mariadb_test(name_test, test_content):
    result = MARIADB_BENCHMARK + " " + test_content + " "
    with open(MARIADB_RELATIVE_PATH + "/" + "mariadb_" + name_test + ".sh", 'w') as f:
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


def generate_mariadb_benchmark_test():
    """
    https://mariadb.com/kb/en/mysqlslap/

    """
    gen_mariadb_test("example_basic", """mysqlslap  \\
 --delimiter=";" \\
 --create="CREATE TABLE t (a int);INSERT INTO t VALUES (5)" \\
 --query="SELECT * FROM t" \\
 --concurrency=40 \\
 --iterations=100 
    """)

    gen_mariadb_test("example_intense", """mysqlslap  \\
 --delimiter=";" \\
 --create="CREATE TABLE t (a int);INSERT INTO t VALUES (5)" \\
 --query="SELECT * FROM t" \\
 --concurrency=40 \\
 --iterations=10000 
    """)


def generate_packers():
    """"""


EXAMPLE_FILE_NAMES = ['XirXinNVTD', 'dtSU9URVgX', 'gT8wwdWudV', 'mZXOjbVYR0', 'urSsNeMZVQ', 'A5wlkU2tqW', 'muNR3nuPMC',
                      'ZOsj93hUnf', 'PgPSCVzBQH', 'BpQD8Vnc5c', 'tGFpEvNrJd', '6fZNcA7WR5', 'y4D9lWwn0d', 'mTsQqK5dRM',
                      'xBXMDud3yN', 'zHWYe9pTtx', 'kPh2hjbLvQ', 'Sb0ERLVHTq', '40ypHOCyRh', 'tdfefTGuYV', 'xbYIUlBEvw',
                      'CJlTJVDdna', 'YUBAAiquDK', 'UOrCDFtfka', 'jJxANuGvu2', 'PfkJo1cwsM', 'RCaJogKaWg', 'MQ6Zzk4zMA',
                      '6AsB1X68iv', '3BU9j4GmOM', 'vxH1y8CrqQ', '4vRlEYt2KP', 'yZXFbHM2pk', 'Mmkrte3m8u', 'Molkk7g8g4',
                      'F0hd3N5gl0', '3aXPrlbUfh', 'ngt6QNTOPd', 'TSETUtNNw6', '5ekCfy1ycQ', 'QjVEeePbBl', 'Gb2Y4A0yKK',
                      'pgPRNb2FUS', '4GYB4KVGcq', '9tvzu34t0r', 'ntB0xVyncF', 'ECaNXMz2xb', 'amTbXmbsmN', 'a0jHmQb8nZ',
                      'uDg1LTwWoJ', 'vfPkCitP76', 'ogXNlDb1zy', '9fCqpkptw7', 'ZG0vWyaNZU', 'N3uglts8W3', 'XHpWW6E1aF',
                      'QMqIdZCMvD', 're3Y6kY2Wu', '2sQbriPJvd', 'e4u3Xyd4P8']

ARCHIVER_RELATIVE_PATH = "archivers/"
ARCHIVED_FILENAME = "file.txt"
ARCHIVED_FOLDER = "folder"

GIT_RELATIVE_PATH = "actions_git/"


def init_archiver_template():
    start = """#!/bin/bash
sleep 5m
    """
    result = start
    for filname in EXAMPLE_FILE_NAMES:
        result = result + "\nbase64 /dev/urandom | head -c 10000000 >" + ARCHIVED_FOLDER + "/" + filname + ".txt"
    return result + "\n"


ARCHIVER_TEMPLATE = init_archiver_template()


def gen_archiver_test(archive_type, archive_content):
    result = ARCHIVER_TEMPLATE + "" + archive_content + " "
    with open(ARCHIVER_RELATIVE_PATH + "/" + "archiver_" + archive_type + ".sh", 'w') as f:
        f.write(result)


def generate_all_archivers():
    """"""
    gen_archiver_test("bzip2", "bzip2 " + ARCHIVED_FOLDER + "/*")
    gen_archiver_test("gzip", "gzip " + ARCHIVED_FOLDER + "/*")
    gen_archiver_test("lrzip", "sudo apt install lrzip\nlrzip " + ARCHIVED_FOLDER + "/*")
    gen_archiver_test("xz", "xz " + ARCHIVED_FOLDER + "/*")
    gen_archiver_test("tar", "tar -xvf " + ARCHIVED_FOLDER + "/*")
    gen_archiver_test("7zip", """
sudo add-apt-repository universe
sudo apt install p7zip-full p7zip-rar
7z e """ + ARCHIVED_FOLDER + "/*")


def gen_git_test(file_type, git_content):
    result = GIT_CONFIG + "" + git_content + " "
    with open(GIT_RELATIVE_PATH + "/" + "git_command_" + file_type + ".sh", 'w') as f:
        f.write(result)


def generate_git_actions():
    create_folder = [GIT_CREATE_ENTER_FOLDER,
                     GIT_SELECT_RAND_PROJECT]
    setup_remote = [GIT_SELECT_RAND_PROJECT]

    file_folder_creation_options = [GIT_CREATE_SINGLE_FILE,
                                    GIT_CREATE_SINGLE_FILE + GIT_CREATE_FOLDER_SINGLE,
                                    GIT_CREATE_SINGLE_FILE + GIT_CREATE_FOLDER_MULTIPLE,
                                    GIT_CREATE_MULTIPLE_FILES,
                                    GIT_CREATE_MULTIPLE_FILES + GIT_CREATE_FOLDER_SINGLE,
                                    GIT_CREATE_MULTIPLE_FILES + GIT_CREATE_FOLDER_MULTIPLE,
                                    ]
    remove_files = [GIT_REMOVE_ALL]
    switch_branches = [GIT_SWITCH_BRANCHES]
    reset_remote = [GIT_RESET_REMOTE]

    #
    all_options = itertools.product(create_folder,
                                    setup_remote,
                                    file_folder_creation_options,
                                    remove_files,
                                    switch_branches,
                                    reset_remote)
    for option in all_options:
        print(option)


if __name__ == '__main__':
    # generate_all_manual()
    # generate_all_snaped()
    # generate_cassandra_benchmark_test()
    # generate_mariadb_benchmark_test()
    # generate_all_archivers()
    generate_git_actions()
