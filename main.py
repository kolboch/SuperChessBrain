import os
import time

from pynput import keyboard
from pynput import mouse


def main():
    _mouse = mouse.Controller()
    _keyboard = keyboard.Controller()
    listener = keyboard.Listener(
        on_press=on_keyboard_press,
        on_release=on_keyboard_release
    )
    listener.start()
    print("current mouse position:", _mouse.position)
    while True:
        time.sleep(0.1)
        pass


def on_keyboard_press(key):
    return


def on_keyboard_release(key):
    if key == keyboard.Key.esc:
        os._exit(0)
    else:
        print(key)


if __name__ == '__main__':
    main()
