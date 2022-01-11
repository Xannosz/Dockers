clear

tput setaf 1;
echo "Set root password:"
tput sgr0;

passwd

clear

type=$(dialog --stdout --menu "Select user:" 15 38 10 "1" "Create new user" "2" "Use existing Windows user")

if [ $type == "1" ]; then
  userName=$(dialog --stdout --inputbox "User name:" 15 38)
else
  userNames=( $(ls /c/Users | grep -v 'All Users\|Default\|Default User\|Public\|desktop.ini') )
  users=$(ls /c/Users | grep -v 'All Users\|Default\|Default User\|Public\|desktop.ini' | awk '{print v++,$0}')
  key=$(dialog --stdout --menu "Select user:" 15 38 10 $users)
  userName=${userNames[$key]};
fi

clear

tput setaf 2;
echo "Set user password:"
tput sgr0;

adduser --gecos '' $userName

usermod -aG sudo $userName

sed -i "s:cd /c/Users:cd /c/Users/${userName}:g" "/home/${userName}/.bashrc"

sed -i "s:<defUser>:${userName}:g" "/etc/wsl.conf"

rm -rf /install

rm  /etc/profile.d/start.sh

exit