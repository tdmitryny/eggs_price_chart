FROM python:3.14.0a5-alpine3.21

#Copy files to docker
COPY requirements.txt /temp/requirements.txt
COPY egg_price /egg_price

#where file are located
WORKDIR /egg_price

#what server to use
EXPOSE 8000


RUN pip install -r /temp/requirements.txt

#Create user
RUN adduser --disabled-password egg_user

USER egg_user
