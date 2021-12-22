#!/bin/bash

FILE='geschenk.txt'
ZIPS='2021'

mkdir -p work
cd work
echo 'DiesIstDasPasswort123' > geschenk.txt

COUNT=0
for I in $(seq 1 $ZIPS); do
        COUNT=$((COUNT+1))
        RAND_NAME=$(shuf -i 100000-999999 -n 1)
        LS=$(ls)
        zip -qq $RAND_NAME.zip $LS
        rm $LS -R
        echo "Zipped: ${COUNT}: File: ${LS}"
done
LAST_FILE=$(ls)
mv $LAST_FILE geschenk.zip

echo
echo '----------------------------------------------'
echo 'File zipped!'
echo "Zipped \"${COUNT}\" times."
echo 'Filename: geschenk.zip'
echo '----------------------------------------------'
