import logging
import time
from prometheus_client import start_http_server, Gauge
import speedtest

Download = Gauge('download_speed', 'Download Speed')
Upload = Gauge('upload_speed', 'Upload Speed')
Ping = Gauge('ping', 'Ping')

logging.basicConfig(filename='test_connection.log', level=logging.DEBUG)

def testSpeed():
    """Calls the speedtest API and returns Download, Upload and Ping"""
    servers = []
    threads = None

    try:
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        Download.set(s.download(threads=threads))
        Upload.set(s.upload(threads=threads))
        Ping.set(s.results.ping)
        logging.info('Speedtest successful')
    except Exception as e:
        logging.error('Speedtest failed: %s', e)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        testSpeed()
        time.sleep(60)
