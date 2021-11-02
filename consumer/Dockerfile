FROM python:3.8-slim

RUN mkdir -p /consumer_app/src

WORKDIR /consumer_app/src

# Installing python dependencies
COPY requirements.txt /consumer_app/src
RUN pip install --no-cache-dir -r requirements.txt

# Copying src code to Container
COPY consumer.py /consumer_app/src/

# Running Python Application
CMD ["python", "-u", "consumer.py"]
