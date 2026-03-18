import pytest
import os
import requests

@pytest.mark.integration
def test_third_party_integrations_and_fallbacks():
    payment_cb = os.environ.get('PAYMENT_CALLBACK_URL')
    sms_mock = os.environ.get('SMS_MOCK_URL')
    if not payment_cb or not sms_mock:
        pytest.skip('Integration endpoints not configured')

    # Simulate payment callback
    r = requests.post(payment_cb, json={'order_id': 'TEST123', 'status': 'paid'}, timeout=5)
    assert r.status_code == 200

    # Simulate SMS/send
    r2 = requests.post(sms_mock, json={'to': '+10000000000', 'message': 'Order confirmed'}, timeout=5)
    assert r2.status_code == 200
