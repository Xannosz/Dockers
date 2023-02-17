#!/bin/bash

echo "############################"
echo "#### `date` ####"
echo "#### run $1 scripts ####"
echo "############################"

while read assignment; do
  export "$assignment"
done < /script/env.txt

env

echo "############################"

for folder in `ls /content`
do
  cd /content/$folder
  if [ -f "./${1}.sh" ]; then
    "./${1}.sh" &
  fi
done