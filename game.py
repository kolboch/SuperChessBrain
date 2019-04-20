import os

from pynput import keyboard
from pynput import mouse
from pynput.keyboard import KeyCode


class Game:

    def __init__(self, state):
        self._state = state
        self._mouse = mouse.Controller()
        self._keyboard = keyboard.Controller()
        self._keyboard_listener = keyboard.Listener(
            on_press=self.on_keyboard_press,
            on_release=self.on_keyboard_release
        )
        self._mouse_listener = None
        self._keyboard_listener.start()

    def on_keyboard_press(self, key):
        return

    def on_keyboard_release(self, key):
        if key == keyboard.Key.esc:
            os._exit(0)
        elif key == KeyCode.from_char('s'):
            # after change of logic this one should be placed in game class
            self.init_setup_board_corners()
            pass
        else:
            print(key)

    def init_setup_board_corners(self):
        if self._mouse_listener is not None:
            self._mouse_listener.stop()
        self._mouse_listener = mouse.Listener(
            on_move=None,
            on_click=self.on_setup_board_corners_click(),
            on_scroll=None
        )
        self._mouse_listener.start()

    def on_setup_board_corners_click(self):
        print('setup board corners click')
        pass
