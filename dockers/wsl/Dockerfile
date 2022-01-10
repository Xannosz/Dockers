FROM ubuntu:latest

COPY ./etc.skel /etc/skel
COPY ./etc.skel/.bashrc /root/.bashrc
COPY ./etc/* /etc/
COPY ./install /install
COPY ./install/start.sh /etc/profile.d/start.sh

ENV LANG en_US.UTF-8

RUN tar xf /install/btop.tbz -C /usr/local bin/btop

RUN apt update
RUN apt -y install dialog htop neofetch ncdu wget curl ssh telnet vim nano

RUN apt -y install mc

RUN apt -y install irssi