FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
