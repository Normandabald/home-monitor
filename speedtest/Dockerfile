FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip
RUN pip3 install --upgrade pip
RUN pip3 install speedtest-cli --upgrade
RUN pip3 install prometheus-client --upgrade

ADD scripts/ /app/speedtest/

RUN chmod +x /app/speedtest/test_connection.py

CMD python3 /app/speedtest/test_connection.py

