#Install curl
tput setaf 7;
tput setab 6;
echo "Install curl"
tput sgr0;
###############
apt update
apt install -y curl
###############

#Create users
tput setaf 7;
tput setab 6;
echo "Create users"
tput sgr0;
###############
tput setaf 1;
echo "Create user xannosz"
tput setaf 2;
adduser xannosz
tput sgr0;
###############

#Install docker
tput setaf 7;
tput setab 6;
echo "Install docker"
tput sgr0;
###############
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x ./get-docker.sh
sh get-docker.sh
usermod -aG docker xannosz
rm ./get-docker.sh
###############

#Create persist folder for blue queen
tput setaf 7;
tput setab 6;
echo "Create persist folder for blue queen"
tput sgr0;
###############
mkdir /persist
chmod 777 /persist
###############

#Docker login
tput setaf 7;
tput setab 6;
echo "Docker login"
tput sgr0;
###############
tput setaf 1;
echo "Docker login"
tput setaf 2;
docker login
tput sgr0;
###############

#Reboot
tput setaf 7;
tput setab 6;
echo "Reboot"
tput sgr0;
###############
reboot
###############