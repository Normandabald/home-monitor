import os
import requests
import time
import datetime
from prometheus_client import start_http_server, Gauge

print("Starting container...")
water_level = Gauge('water_level', 'Water level of river')
water_level_timestamp = Gauge('water_level_timestamp', 'Time when last reading was taken')
station_id = os.getenv('RIVER_STATION_ID')
# station_id = "E2814"
print("Starting to monitor river levels for station: "+str(station_id))
def check_riverlevels():
    try:
        response = requests.get("https://environment.data.gov.uk/flood-monitoring/id/measures/"+str(station_id)+"-level-stage-i-15_min-mASD")
    # Set the Exporter value
        water_level.set(response.json()['items']['latestReading']['value'])

        reading_taken = response.json()['items']['latestReading']['dateTime']
        # Convert DateTime Str to unix timestamp
        date_time_obj = datetime.datetime.strptime(reading_taken, '%Y-%m-%dT%H:%M:%SZ')
        timestamp = (date_time_obj.timestamp())

        water_level_timestamp.set(timestamp)
        print("River level is: "+str(response.json()['items']['latestReading']['value'])+" at: "+str(reading_taken))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8001)
    # Periodically get river level data
    while True:
	    check_riverlevels()
	    time.sleep(100)