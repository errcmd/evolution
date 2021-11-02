FROM python:3.8-slim

RUN mkdir -p /producer_app/src

WORKDIR /producer_app/src

# Installing python dependencies
COPY requirements.txt /producer_app/src
RUN pip install --no-cache-dir -r requirements.txt

# Copying src code to Container
COPY producer.py /producer_app/src/

# Running Python Application
CMD ["python", "-u", "producer.py"]
