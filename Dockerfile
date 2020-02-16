FROM ubuntu:18.04

ENV DEBUG=False
ENV SECRET_KEY=sqw5%^e4lc$dkor-@&5@(csveaw@sdq^mq-nu_u_qy@zel@=u1
ENV LANGUAGE_CODE=pt-br
ENV TIME_ZONE=UTC

ENV DB_ENGINE=django.db.backends.postgresql_psycopg2
ENV DB_NAME=projectbbk
ENV DB_USER=docker
ENV DB_PASSWORD=docker
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432

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
