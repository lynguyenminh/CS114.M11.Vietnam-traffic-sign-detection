FROM ubuntu:18.04

RUN apt update &&\
    apt install software-properties-common -y &&\
    add-apt-repository ppa:deadsnakes/ppa -y &&\
    apt install python3.8 -y

RUN alias python3=python3.8

RUN apt update &&\
    apt install python3-pip -y &&\
    pip3 install --upgrade pip