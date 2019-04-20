import time

from game import Game
from state import State


def main():
    state = State()
    game = Game(state)
    while True:
        time.sleep(0.1)
        pass


if __name__ == '__main__':
    main()
