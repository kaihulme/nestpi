FROM python:3.8-alpine

WORKDIR /app
COPY . .

# install dependencies
RUN \
	apk add g++ \
	&& pip install -r requirements.txt

# initialise database
RUN flask init-db

# run flask application with gunicorn wsgi
EXPOSE 5000
ENTRYPOINT ["gunicorn"] 
CMD ["--bind", "0.0.0.0:5000", "nestpi:create_app()"]
