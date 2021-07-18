#!/bin/bash

# install git
sudo apt install git-all -y

# setup credentials
git config --global user.name "yosi cohen"
git config --global user.email "yonicohen187@gmail.com"

# create and enter folder
mkdir test
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


# change to a new branch
git checkout -b 3d_printer
git add *
git commit -m "changed branch"


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
 