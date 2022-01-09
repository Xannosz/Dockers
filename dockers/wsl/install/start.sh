ls /mnt/c/Users | grep -v 'All Users\|Default\|Default User\|Public\|desktop.ini'

answer=$(dialog --stdout --menu "Select user:" 15 38 10 "1" "Create new user" "2" "Use existing Windows user")

dialog --menu "Select user:" 15 38 10 "1" "User" "2" "New User"

userName=$(dialog --stdout --inputbox "User name:" 15 38 10)

adduser --gecos '' "$userName"

sed -i "s:cd /c/Users:cd /c/Users/${userName}:g" "/home/${userName}/.bashrc"

sed -i "s:command = /install/start.sh:command = :g" "/etc/wsl.conf"

rm -rf /install

su $userName