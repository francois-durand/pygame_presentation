from weakref import WeakKeyDictionary
from collections import defaultdict


class EventManager:
    LISTENS = 1
    """
    Coordinates all communication between models, views and controllers.
    Is responsible for receiving and dispatching all kinds of events.
    """
    def __init__(self):
        """Constructs an empty EventManager object."""
        self._listeners = defaultdict(lambda: WeakKeyDictionary())

    def register_listener(self, listener, events_classes):
        """Registers the listener so it can be notified of events."""
        for event_class in events_classes:
            self._listeners[event_class][listener] = self.LISTENS

    def unregister_listener(self, listener):
        """Unregisters a listener."""
        for event_class in self._listeners:
            self._listeners[event_class].pop(listener, None)

    def post_event(self, event):
        """Posts an event to the concerned listeners."""
        for listener in self._listeners[event.__class__]:
            listener.notify(event)
