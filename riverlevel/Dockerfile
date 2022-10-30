FROM alpine:latest

RUN apk add --update --no-cache py-pip
RUN pip install --upgrade pip
RUN pip install prometheus-client --upgrade
RUN pip install requests
RUN pip install datetime
ENV RIVER_STATION_ID=$RIVER_STATION_ID

ADD scripts/ /app/riverlevels/

RUN chmod +x /app/riverlevels/riverlevels.py

CMD python3 /app/riverlevels/riverlevels.py

