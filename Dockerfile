FROM python:3.7.2-stretch

WORKDIR /projectbbk

COPY . /projectbbk

RUN pip install --upgrade pip
RUN pip install uwsgi
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8080

CMD [ "uwsgi", "wsgi.ini" ]