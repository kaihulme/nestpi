FROM python:alpine3.8

COPY . /app
WORKDIR /app

RUN \
	pip install --upgrade pip \
	&& pip install -r requirements.txt

