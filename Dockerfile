FROM python:3.7.2-stretch

WORKDIR /projectbbk

ADD . /projectbbk

RUN pip install --upgrade pip
RUN pip install uwsgi
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "uwsgi", "app.ini" ]