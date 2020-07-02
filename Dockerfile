FROM python:3.8

RUN apt-get update && apt-get install -y python3-pip gcc

RUN pip3 install --upgrade pip

#Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

WORKDIR /app
