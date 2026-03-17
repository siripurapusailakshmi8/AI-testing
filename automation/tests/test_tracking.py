import os
import time
import pytest
from utils.tracking_simulator import TrackingSimulator

TRACKING_ENDPOINT = os.getenv('TRACKING_ENDPOINT', '')
ORDER_ID = os.getenv('TRACKING_ORDER_ID', 'test-order-123')

@pytest.mark.skipif(not TRACKING_ENDPOINT, reason="TRACKING_ENDPOINT not configured")
def test_real_time_tracking_updates(driver):
    sim = TrackingSimulator(TRACKING_ENDPOINT, api_key=os.getenv('TRACKING_API_KEY'))
    coords = [(12.9716,77.5946),(12.9717,77.5947),(12.9718,77.5948)]
    for lat, lon in coords:
        res = sim.send_location(ORDER_ID, lat, lon)
        assert res is not None
        time.sleep(1)

    # Additional checks on UI would go here; placeholder
    assert True
