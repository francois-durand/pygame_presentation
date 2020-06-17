import pygame as pg
from my_lib.events.listener import Listener
from my_lib.events.events import TickEvent, KeyboardEvent, MainEvent
from my_lib.events.events import MouseButtonEvent, MousePositionEvent


class PgEventController(Listener):
    def __init__(self, event_manager):
        Listener.__init__(
            self,
            event_manager,
            [TickEvent]
        )

    def notify(self, event):
        for pg_event in pg.event.get():
            if pg_event.type == pg.QUIT:
                self.post_event(
                    MainEvent(MainEvent.EXIT_GAME)
                )

            elif pg_event.type == pg.MOUSEBUTTONDOWN:
                self.post_event(
                    MouseButtonEvent(MouseButtonEvent.BUTTON_DOWN)
                )

            elif pg_event.type == pg.MOUSEMOTION:
                self.post_event(
                    MousePositionEvent(pg.mouse.get_pos())
                )

            elif pg_event.type == pg.MOUSEBUTTONUP:
                self.post_event(
                    MouseButtonEvent(MouseButtonEvent.BUTTON_UP)
                )

            elif pg_event.type == pg.KEYDOWN:
                self.post_event(
                    KeyboardEvent(pg_event.key)
                )
