FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /labo
WORKDIR /labo
ADD app/requirements.txt /labo/
RUN pip3 install -r requirements.txt
ADD ./app/labo /labo/
VOLUME ./app/labo:/labo
