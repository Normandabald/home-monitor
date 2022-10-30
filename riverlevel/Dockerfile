FROM alpine:latest

RUN apk add --update --no-cache py-pip
RUN pip install --upgrade pip
RUN pip install prometheus-client --upgrade

ADD scripts/ /app/riverlevels/

RUN chmod +x /app/riverlevels/riverlevels.py

CMD python3 /app/riverlevels/riverlevels.py

