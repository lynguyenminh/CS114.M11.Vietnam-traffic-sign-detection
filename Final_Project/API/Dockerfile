FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8

RUN apt update &&\
    apt install python3-pip -y &&\
    pip3 install --upgrade pip

WORKDIR /api

COPY . .

RUN pip3 install cachetools

RUN pip3 install -r requirements.txt

CMD [ "python3" "app.py" ]