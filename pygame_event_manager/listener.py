class Listener:
    """
    Abstract class for listeners. Possesses an event manager as attribute.
    Can post event to the event manager, and can be notified of events.
    """
    def __init__(self, event_manager, events_classes):
        """Constructor."""
        self._event_manager = event_manager
        self.register(events_classes)

    def register(self, events_classes):
        """Register itself to the event manager"""
        self._event_manager.register_listener(self, events_classes)

    def notify(self):
        """Gets notified of an event"""
        pass

    def post_event(self, event):
        """post an event to be dispatched by the event manager"""
        self._event_manager.post_event(event)
