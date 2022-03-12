FROM python:3.9-alpine

WORKDIR /app
COPY . .

# quiet flag to supress root user warnings
RUN pip install -r requirements.txt -qqq

ENTRYPOINT ["python3"]
CMD ["app.py"]
