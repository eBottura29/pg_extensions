from pg_extensions import *


def start():
    pass


def update():
    window = get_window()
    set_window(window)


if __name__ == "__main__":
    run(start, update)
