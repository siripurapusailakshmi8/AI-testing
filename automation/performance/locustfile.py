from locust import HttpUser, task, between
import random

class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def browse_and_view(self):
        self.client.get("/")
        self.client.get("/restaurants")

    @task(1)
    def place_order(self):
        # Simplified API-based order placement - endpoints must exist in staging
        restaurants = self.client.get('/api/restaurants').json()
        if not restaurants:
            return
        r = random.choice(restaurants)
        menu = self.client.get(f"/api/restaurants/{r['id']}/menu").json()
        if not menu:
            return
        items = random.sample(menu, min(2, len(menu)))
        order = {"user_id": "load-test-user", "items": [i['id'] for i in items], "payment": {"method": "sandbox"}}
        res = self.client.post('/api/orders', json=order)
        if res.status_code in (200,201):
            pass
