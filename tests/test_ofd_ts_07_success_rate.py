import pytest
import os
import requests

@pytest.mark.load
def test_order_placement_success_rate_placeholder():
    api = os.environ.get('ORDER_API_URL')
    if not api:
        pytest.skip('ORDER_API_URL not configured')

    attempts = int(os.environ.get('BULK_ATTEMPTS', '10'))
    success = 0
    for i in range(attempts):
        r = requests.post(f'{api}/orders', json={'test': True}, timeout=10)
        if r.status_code in (200,201):
            success += 1
    success_rate = (success / attempts) * 100
    assert success_rate >= 95, f'Success rate too low: {success_rate}%'
