echo ""
echo "############################"
echo "#### `date` ####"
echo "#### run $1 scripts ####"
echo "############################"

for folder in `ls /content`
do
  cd /content/$folder
  if [ -f "./${1}.sh" ]; then
    "./${1}.sh" &
  fi
done