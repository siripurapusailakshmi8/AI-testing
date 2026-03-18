import time
from pages.tracking_page import TrackingPage


def test_real_time_tracking(driver, base_url, api_client, test_order):
    tracking = TrackingPage(driver, base_url)

    order_id = test_order['order_id']
    # Step 2
    tracking.open_tracking(order_id)
    assert tracking.has_map()

    # Step 3 - inject events via API/mock
    events = [
        {'status': 'Out for delivery', 'lat': 40.0, 'lng': -70.0},
        {'status': 'Delivered', 'lat': 40.01, 'lng': -70.01}
    ]
    for e in events:
        api_client.post(f"/tracking/{order_id}", json=e)
        time.sleep(1)
        # Step 4-5: verify UI updates (simple wait + assert)
        status = tracking.get_status()
        assert e['status'] in status

    # Final check
    assert 'Delivered' in tracking.get_status()
