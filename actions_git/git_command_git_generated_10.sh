#!/bin/bash

# install git
sudo apt install git-all -y

# setup credentials
git config --global user.name "yosi cohen"
git config --global user.email "yonicohen187@gmail.com"

# select random project from top 100
allProjects=("https://github.com/freeCodeCamp/freeCodeCamp" "https://github.com/996icu/996.ICU" "https://github.com/EbookFoundation/free-programming-books" "https://github.com/vuejs/vue" "https://github.com/jwasham/coding-interview-university" "https://github.com/sindresorhus/awesome" "https://github.com/kamranahmedse/developer-roadmap" "https://github.com/tensorflow/tensorflow" "https://github.com/twbs/bootstrap" "https://github.com/getify/You-Dont-Know-JS" "https://github.com/public-apis/public-apis" "https://github.com/donnemartin/system-design-primer" "https://github.com/ohmyzsh/ohmyzsh" "https://github.com/flutter/flutter" "https://github.com/github/gitignore" "https://github.com/microsoft/vscode" "https://github.com/torvalds/linux" "https://github.com/trekhleb/javascript-algorithms" "https://github.com/danistefanovic/build-your-own-x" "https://github.com/TheAlgorithms/Python" "https://github.com/airbnb/javascript" "https://github.com/Snailclimb/JavaGuide" "https://github.com/jackfrued/Python-100-Days" "https://github.com/d3/d3" "https://github.com/ytdl-org/youtube-dl" "https://github.com/facebook/react-native" "https://github.com/electron/electron" "https://github.com/jlevy/the-art-of-command-line" "https://github.com/ossu/computer-science" "https://github.com/axios/axios" "https://github.com/justjavac/free-programming-books-zh_CN" "https://github.com/nodejs/node" "https://github.com/kubernetes/kubernetes" "https://github.com/microsoft/terminal" "https://github.com/angular/angular" "https://github.com/microsoft/TypeScript" "https://github.com/mrdoob/three.js" "https://github.com/puppeteer/puppeteer" "https://github.com/animate-css/animate.css" "https://github.com/tensorflow/models" "https://github.com/vercel/next.js" "https://github.com/mui-org/material-ui" "https://github.com/PanJiaChen/vue-element-admin" "https://github.com/iluwatar/java-design-patterns" "https://github.com/goldbergyoni/nodebestpractices" "https://github.com/laravel/laravel" "https://github.com/FortAwesome/Font-Awesome" "https://github.com/avelino/awesome-go" "https://github.com/MisterBooo/LeetCodeAnimation" "https://github.com/storybookjs/storybook" "https://github.com/nvbn/thefuck" "https://github.com/moby/moby" "https://github.com/angular/angular.js" "https://github.com/gothinkster/realworld" "https://github.com/webpack/webpack" "https://github.com/django/django" "https://github.com/microsoft/PowerToys" "https://github.com/tonsky/FiraCode" "https://github.com/rust-lang/rust" "https://github.com/apple/swift" "https://github.com/reduxjs/redux" "https://github.com/spring-projects/spring-boot" "https://github.com/pallets/flask" "https://github.com/atom/atom" "https://github.com/elastic/elasticsearch" "https://github.com/bitcoin/bitcoin" "https://github.com/opencv/opencv" "https://github.com/yangshun/tech-interview-handbook" "https://github.com/doocs/advanced-java" "https://github.com/netdata/netdata" "https://github.com/typicode/json-server" "https://github.com/jquery/jquery" "https://github.com/thedaviddias/Front-End-Checklist" "https://github.com/chartjs/Chart.js" "https://github.com/socketio/socket.io" "https://github.com/expressjs/express" "https://github.com/xingshaocheng/architect-awesome" "https://github.com/kdn251/interviews" "https://github.com/gohugoio/hugo" "https://github.com/adam-p/markdown-here" "https://github.com/tuvtran/project-based-learning" "https://github.com/keras-team/keras" "https://github.com/Genymobile/scrcpy" "https://github.com/httpie/httpie" "https://github.com/chrislgarry/Apollo-11" "https://github.com/h5bp/html5-boilerplate" "https://github.com/josephmisiti/awesome-machine-learning" "https://github.com/ElemeFE/element" "https://github.com/redis/redis" "https://github.com/lodash/lodash" "https://github.com/nvm-sh/nvm" "https://github.com/h5bp/Front-end-Developer-Interview-Questions" "https://github.com/gin-gonic/gin" "https://github.com/Semantic-Org/Semantic-UI" "https://github.com/pytorch/pytorch" "https://github.com/resume/resume.github.com" "https://github.com/ansible/ansible" "https://github.com/protocolbuffers/protobuf" "https://github.com/rails/rails" "https://github.com/sveltejs/svelte")
rand=$[$RANDOM % ${#allProjects[@]}]
project=${allProjects[$rand]}

git clone $project test
cd test

git add *
git commit -m "first commit"

git remote add origin master ""

# create multiple files

## init random amount of files

## add tje files to git

## commit the files
echo "first file" >> README.md
git add README.md
git commit -m "added multiple files"


# create a multiple folders
declare -a arr=(1..10)

## now loop through the above array
for i in "${arr[@]}"
  mkdir example_folder
  touch example_folder/file${i}.txt
  git add *  
done 

git commit -m "added folders"


# remove files git
git rm * -r
git add * 
git commit -m "removed all files"



# changing back
git checkout -b master
git add *
git commit -m "changed back"


# create multiple files

## init random amount of files

## add tje files to git

## commit the files
echo "first file" >> README.md
git add README.md
git commit -m "added multiple files"


# create a multiple folders
declare -a arr=(1..10)

## now loop through the above array
for i in "${arr[@]}"
  mkdir example_folder
  touch example_folder/file${i}.txt
  git add *  
done 

git commit -m "added folders"


# remove files git
git rm * -r
git add * 
git commit -m "removed all files"


# remove files git
git rm * -r
git add * 
git commit -m "removed all files"


# remote all files from remote
git rm *
git commit -m "removed all"
 