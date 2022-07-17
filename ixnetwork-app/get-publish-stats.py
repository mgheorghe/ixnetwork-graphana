from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

TX_RATE = Gauge('TX_RATE_bytes', 'transmit byte rate')
RX_RATE = Gauge('RX_RATE_bytes', 'receive byte rate')

# Decorate function with metric.
def get_ixnetwork_stats():
    """A dummy function that takes some time."""
    TX_RATE.set(random.randint(1,1000))
    RX_RATE.set(random.randint(1,1000))
    time.sleep(1)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        get_ixnetwork_stats()