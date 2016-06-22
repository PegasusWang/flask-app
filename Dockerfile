FROM python:2.7.11
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
