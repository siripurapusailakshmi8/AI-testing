import requests
import time

class TrackingSimulator:
    def __init__(self, endpoint, api_key=None):
        self.endpoint = endpoint
        self.api_key = api_key

    def send_location(self, order_id, lat, lon):
        payload = {"order_id": order_id, "latitude": lat, "longitude": lon}
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        resp = requests.post(self.endpoint, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()
