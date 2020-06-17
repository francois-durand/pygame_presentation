class Event:
    def __init__(self):
        pass


class TickEvent(Event):
    def __init__(self):
        pass


class MainEvent(Event):
    EXIT_GAME = 'exit_game'
    START_PVP_GAME = 'start_pvp_game'

    def __init__(self, event_str):
        self._event_str = event_str

    def get_event(self):
        return self._event_str


class KeyboardEvent(Event):
    def __init__(self, key):
        self._key = key

    def get_key(self):
        return self._key


class MousePositionEvent(Event):
    def __init__(self, position):
        self._position = position

    def get_position(self):
        return self._position


class MouseButtonEvent(Event):
    BUTTON_UP = 'button_up'
    BUTTON_DOWN = 'button_down'

    def __init__(self, event_str):
        self._event_str = event_str

    def get_event(self):
        return self._event_str


class ViewEvent(Event):
    def __init__(self, event_str):
        self._event_as_str = event_str


class MenuEvent(Event):
    SHOW_MAIN_MENU = 'show_main_menu'
    HIDE_MAIN_MENU = 'hide_main_menu'

    def __init__(self, event_str):
        self._event_str = event_str

    def get_event(self):
        return self._event_str


class GameEvent(Event):
    START_PVP_GAME = 'start_pvp_game'
    GAME_VIEW_START_DISPLAY = 'game_view_start_display'

    def __init__(self, event_str):
        self._event_str = event_str

    def get_event(self):
        return self._event_str
