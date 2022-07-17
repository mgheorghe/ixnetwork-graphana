FROM python:3.9-slim-buster

WORKDIR /ixnetwork-app

RUN apt update

RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ixnetwork-app

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/ixnetwork-app

CMD ["python3", "ixnetwork-app/get-publish-stats.py"]