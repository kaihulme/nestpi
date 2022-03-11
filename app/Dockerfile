FROM python:alpine3.8

WORKDIR /app
COPY requirements.txt /app

RUN \
	pip install --upgrade pip \
	&& pip install -r requirements.txt

COPY . /app

