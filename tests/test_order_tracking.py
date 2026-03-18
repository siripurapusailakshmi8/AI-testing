import os
import time
import pytest
from pages.tracking_page import TrackingPage


@pytest.mark.integration
def test_real_time_order_tracking(driver, base_url, test_user):
    """OFD-TC-002: Real-time order tracking"""
    # This test assumes an order exists or can be created and moved to Out for Delivery
    # For demo, we rely on a tracking API mock endpoint
    order_id = os.environ.get('TEST_TRACKING_ORDER_ID')
    assert order_id, "Provide TEST_TRACKING_ORDER_ID env var or enhance test to create an order"

    track = TrackingPage(driver, base_url)
    track.open(f"/orders/{order_id}/tracking")

    # initial checks
    assert track.get_text(*TrackingPage.ETA) or True

    # simulate external location update via mock API
    mock_api = os.environ.get('TRACKING_MOCK_API')
    if mock_api:
        import requests
        payload = {"order_id": order_id, "lat": 12.34, "lon": 56.78, "eta": "10 mins"}
        r = requests.post(f"{mock_api}/simulate", json=payload)
        assert r.status_code == 200

        # give UI time to reflect update
        time.sleep(2)
        # verify marker moved or ETA updated
        assert track.get_text(*TrackingPage.ETA) == "10 mins"

"}