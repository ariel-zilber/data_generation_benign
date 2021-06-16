#!/bin/bash

# reset file
echo "" >snap-list.txt

# search packages
for x in {{a..z},{A..Z},{1..9}}
do
  echo "Letter: ${x}"
  snap find "${x}" | awk '{if ($1!="Name") print $1}' >> snap-list.txt
done


# remove repeating
cat snap-list.txt  | sort| uniq > snap-list-uniq.txt
rm snap-list.txt
mv snap-list-uniq.txt snap-list.txt



# get install python command
#cat snap-list.txt | awk '{print "install_basic(\""$1"\", \"sudo snap install "$1"\")"}' > command.txt
#rm snap-list.txt
#mv command.txt snap-list.txt

