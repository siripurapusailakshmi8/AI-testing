import pytest
import os
import requests

# Payment tests use sandbox endpoints; real credentials and endpoints must be configured via env vars

@pytest.mark.payment
def test_payment_success_and_failure_flows():
    sandbox_url = os.environ.get('PAYMENT_SANDBOX_URL')
    if not sandbox_url:
        pytest.skip('PAYMENT_SANDBOX_URL not configured')

    # Example: Simulate a successful card payment via sandbox API
    payload = {'amount': 1.0, 'method': 'card', 'card': '4111111111111111'}
    r = requests.post(f'{sandbox_url}/pay', json=payload, timeout=10)
    assert r.status_code in (200,201)
    data = r.json()
    assert data.get('status') in ('success','approved')

    # Simulate a declined card
    payload['card'] = '4000000000000002'
    r2 = requests.post(f'{sandbox_url}/pay', json=payload, timeout=10)
    assert r2.status_code in (200,402,400)
    # Expect decline handling
