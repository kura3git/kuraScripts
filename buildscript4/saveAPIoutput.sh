#!/bin/bash

while read url;
do
# run api call for each image URL from imageURLs file
python3 python_dev_final.py $url > output.txt

mkdir -p ./image_tags

sed -e 's/[{}'\'']//g' < ./output.txt | tr "," "\n" | \
# save txt file with tags and probabilties appending
# last substring of image URL as the identifier
sed 's/^[ /t]*//;s/[ \t]*$//' > ./image_tags/tags_${url##*/}.txt;
done < ./imageURLs.txt


