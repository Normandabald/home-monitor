FROM alpine:latest

RUN apk add --update --no-cache py-pip curl bash
RUN pip install --upgrade pip
RUN pip install speedtest-cli --upgrade
RUN pip install prometheus-client --upgrade

ADD scripts/ /app/speedtest/

RUN chmod +x /app/speedtest/test_connection.py

CMD python3 /app/speedtest/test_connection.py

