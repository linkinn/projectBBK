FROM ubuntu:18.04

RUN apt update && apt upgrade \
    apt install software-properties-common \
    add-apt-repository ppa:deadsnakes/ppa \
    apt install build-essential \
    apt install python3.8 \
    ln -sf /usr/bin/python3.8 /usr/bin/python \
    apt install python3-pip \
    apt install python3.8-dev \
    apt install git \
    pip3 install --upgrade pip \
    pip3 install wheel \
    pip3 install uwsgi \
    git clone https://github.com/linkinn/projectBBK.git \
    cd projectBBK \
    pip3 install -r requirements.txt \
    uwsgi --http :8080 --module projectBBK.wsgi

EXPOSE 8080
