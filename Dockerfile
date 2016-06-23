FROM python:2.7.11
ADD . /flask-app
WORKDIR /flask-app
EXPOSE 5000
RUN apt-get update
RUN pip install -r requirements.txt
