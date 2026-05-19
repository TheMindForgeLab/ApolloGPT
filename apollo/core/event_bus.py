class EventBus:
    def __init__(self):
        self.events = []

    def publish(self, event_type, payload):
        self.events.append({"type": event_type, "payload": payload})

