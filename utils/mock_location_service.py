import time

class MockLocationService:
    """A very small stub to simulate emitting location updates to a backend.
    In real usage this would call an API or message broker to push location events.
    """
    def __init__(self, order_id):
        self.order_id = order_id

    def emit_sequence(self, seq, delay=1):
        for loc in seq:
            # In real use case, POST to tracking endpoint
            print(f"Emitting for {self.order_id}: {loc}")
            time.sleep(delay)
