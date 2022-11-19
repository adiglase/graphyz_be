FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get -y install build-essential libssl-dev libffi-dev python3-dev python-dev

WORKDIR /backend-django

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .