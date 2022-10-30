FROM alpine:latest

RUN apk add --update --no-cache py-pip
RUN pip install --upgrade pip
RUN pip install speedtest-cli --upgrade
RUN pip install prometheus-client --upgrade
ENV STATION_ID=$STATION_ID

ADD scripts/ /app/speedtest/

RUN chmod +x /app/speedtest/test_connection.py

CMD python3 /app/speedtest/test_connection.py

