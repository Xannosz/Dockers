ls /c/Users | grep -v 'All Users\|Default\|Default User\|Public\|desktop.ini'

type=$(dialog --stdout --menu "Select user:" 15 38 10 "1" "Create new user" "2" "Use existing Windows user")

if [ $type == "1" ]; then
  userName=$(dialog --stdout --inputbox "User name:" 15 38)
else
  userNames=( $(ls /c/Users | grep -v 'All Users\|Default\|Default User') )
  users=$(ls /c/Users | grep -v 'All Users\|Default\|Default User' | awk '{print v++,$0}')
  key=$(dialog --stdout --menu "Select user:" $((${#users[@]}+12)) 38 ${#users[@]} $users)
  userName=${userNames[$key]};
fi

adduser --gecos '' $userName

sed -i "s:cd /c/Users:cd /c/Users/${userName}:g" "/home/${userName}/.bashrc"

sed -i "s:<defUser>:${userName}:g" "/etc/wsl.conf"

sed -i "s:command = \"/install/start.sh\":command = :g" "/etc/wsl.conf"

rm -rf /install

su $userName