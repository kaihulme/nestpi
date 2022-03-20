FROM python:3.8-alpine

WORKDIR /app
COPY . .

RUN \
	apk add build-base \
	&& pip install -r requirements.txt

# initialise database
RUN flask init-db

EXPOSE 5000

# run flask application with gunicorn wsgi
ENTRYPOINT ["gunicorn"] 
CMD ["--bind", "0.0.0.0:5000", "nestpi:create_app()"]
