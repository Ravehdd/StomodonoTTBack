FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt


ADD . /code/
#ADD .env.docker /code/.env

RUN mkdir -p /code/static


CMD python manage.py migrate


ENV APP_NAME=Stomodono

#RUN pip install -r requirements.txt

CMD gunicorn dbsite.wsgi:application -b 0.0.0.0:8000
#CMD python manage.py runserver 0.0.0.0:8000