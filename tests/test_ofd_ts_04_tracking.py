import pytest
import os
import requests

@pytest.mark.integration
def test_real_time_order_tracking_mock():
    tracking_api = os.environ.get('TRACKING_API_URL')
    order_id = os.environ.get('TRACKING_TEST_ORDER_ID')
    if not tracking_api or not order_id:
        pytest.skip('TRACKING_API_URL or TRACKING_TEST_ORDER_ID not configured')

    # Push location updates (mock)
    updates = [
        {'status': 'picked-up', 'lat': 12.34, 'lon': 56.78},
        {'status': 'en-route', 'lat': 12.35, 'lon': 56.79},
        {'status': 'near', 'lat': 12.36, 'lon': 56.80},
        {'status': 'delivered', 'lat': 12.37, 'lon': 56.81},
    ]
    for u in updates:
        r = requests.post(f'{tracking_api}/orders/{order_id}/update', json=u, timeout=5)
        assert r.status_code == 200
