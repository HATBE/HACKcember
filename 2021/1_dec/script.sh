#!/bin/bash

# https://www.floriandalwigk.de/santas-geschenk-hackcember-1

mkdir -p work
wget https://s6cc09bec31deaeb6.jimcontent.com/download/version/1638217360/module/12930298726/name/geschenk.zip -O work/geschenk.zip -q
echo 'Downloaded: geschenk.zip'

cd work

COUNT=0
LOOP=true

while $LOOP; do
        LS=$(ls)
        if ! [[ $LS = *.zip ]]; then
                FILE_NAME=$LS
                LOOP=false
                continue
        fi
        COUNT=$((COUNT+1))
        unzip -qq $LS
        rm $LS -R
        echo "${COUNT}: File: ${LS}"
done

PW=$(cat $FILE_NAME)

echo
echo '----------------------------------------------'
echo 'File found!'
echo "Unpacked \"${COUNT}\" archives."
echo "Filename: \"${FILE_NAME}\""
echo '----------------------------------------------'
echo "The Password is \"${PW}\""
echo '----------------------------------------------'
