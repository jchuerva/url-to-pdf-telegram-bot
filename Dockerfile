FROM balenalib/raspberry-pi2-alpine-python:3.7.4-edge-build-20191011

RUN apt-get install wkhtmltopdf

RUN curl -LOk https://github.com/jchuerva/url-to-pdf-telegram-bot/archive/raspberrypi.zip
RUN unzip -o master.zip

RUN apk add --update tzdata
ENV TZ=Europe/Madrid

WORKDIR /hmtl-to-pdf-bot-master

RUN pip install -r requirements.txt
CMD python /hmtl-to-pdf-bot-master/bot.py