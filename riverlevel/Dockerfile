FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip
RUN pip3 install --upgrade pip
RUN pip3 install prometheus-client --upgrade
RUN pip3 install requests
RUN pip3 install datetime

ADD scripts/ /app/riverlevels/

RUN chmod +x /app/riverlevels/riverlevels.py

CMD python3 /app/riverlevels/riverlevels.py
