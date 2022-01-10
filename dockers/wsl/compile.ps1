docker export -o osb.tar.gz wsl
wsl --unregister osbandi
wsl --import osbandi C:\wsldistros\osbandi .\osb.tar.gz --version 2
wsl -d osbandi