import pygame as pg

from my_lib.events.listener import Listener
from my_lib.events.events import TickEvent


class TickController(Listener):
    def __init__(self, event_manager, config_obj):
        """Constructor. Registers as listener and init the game tick clock"""
        # register as a listener
        Listener.__init__(
            self,
            event_manager,
            []
        )
        # get fps from config and init pygame clock
        self._frame_rate = config_obj.get_fps()
        self._clock = pg.time.Clock()

    def run(self):
        """Main game loop. Sends a tick event on each tick"""
        self._keep_ticking = True
        while self._keep_ticking:
            self.tick()

    def tick(self):
        """Uses pygame clock to tick regularly, and posts a tick event """
        self._clock.tick(self._frame_rate)
        self.post_event(TickEvent())
