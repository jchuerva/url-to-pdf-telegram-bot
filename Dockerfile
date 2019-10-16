FROM balenalib/raspberry-pi2-alpine-python:3.7.4-edge-build-20191011

RUN apt-get install wkhtmltopdf

RUN curl -LOk https://github.com/jchuerva/url-to-pdf-telegram-bot/archive/raspberrypi.zip
RUN unzip -o raspberrypi.zip

RUN apk add --update tzdata
ENV TZ=Europe/Madrid

WORKDIR /url-to-pdf-telegram-bot-raspberrypi

RUN pip install -r requirements.txt
CMD python /url-to-pdf-telegram-bot-raspberrypi/bot.py