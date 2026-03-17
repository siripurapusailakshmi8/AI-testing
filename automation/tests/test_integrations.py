import os
import requests
import pytest

PAYMENT_WEBHOOK = os.getenv('PAYMENT_WEBHOOK', '')
NOTIF_MOCK_ENDPOINT = os.getenv('NOTIF_MOCK_ENDPOINT', '')
LOCATION_API = os.getenv('LOCATION_API', '')

@pytest.mark.skipif(not PAYMENT_WEBHOOK, reason="PAYMENT_WEBHOOK not configured")
def test_payment_and_notification_flow():
    # Simulate payment gateway callback
    payload = {"order_id": "test-123", "status": "success", "amount": 100}
    r = requests.post(PAYMENT_WEBHOOK, json=payload, timeout=10)
    assert r.status_code in (200,201)

@pytest.mark.skipif(not NOTIF_MOCK_ENDPOINT, reason="NOTIF_MOCK_ENDPOINT not configured")
def test_notification_sent():
    payload = {"to": "+10000000000", "message": "Order confirmed"}
    r = requests.post(NOTIF_MOCK_ENDPOINT, json=payload, timeout=10)
    assert r.status_code in (200,201)

@pytest.mark.skipif(not LOCATION_API, reason="LOCATION_API not configured")
def test_location_service():
    params = {"address": "1600 Amphitheatre Parkway, Mountain View"}
    r = requests.get(LOCATION_API, params=params, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert "lat" in data or "results" in data
