FROM python:3.9-alpine

WORKDIR /app
COPY . .

# quiet flag to supress root user warnings
RUN pip install -r requirements.txt -qqq

EXPOSE 5000

# initialise database
RUN flask init-db

# run flask application
RUN flask run --host=0.0.0.0