FROM rackspacedot/python37

RUN apt-get install wkhtmltopdf

RUN curl -LOk https://github.com/jchuerva/hmtl-to-pdf-bot-master/archive/master.zip
RUN unzip -o master.zip

RUN apk add --update tzdata
ENV TZ=Europe/Madrid

WORKDIR /hmtl-to-pdf-bot-master

RUN pip install -r requirements.txt
CMD python /hmtl-to-pdf-bot-master/bot.py