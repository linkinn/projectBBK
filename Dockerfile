FROM ubuntu:18.04

RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.8 -y
RUN ln -sf /usr/bin/python3.8 /usr/bin/python
