FROM ubuntu:latest

COPY ./etc.skel /etc/skel
COPY ./etc.skel/.bashrc /root/.bashrc
COPY ./etc/* /etc/
COPY ./install /install

ENV LANG en_US.UTF-8

RUN tar xf /install/btop.tbz -C /usr/local bin/btop

RUN apt update
RUN apt -y install dialog htop neofetch ncdu wget curl ssh telnet

RUN apt -y install mc

RUN apt -y install irssi