FROM python:3.10

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r "requirements.txt"

COPY . .