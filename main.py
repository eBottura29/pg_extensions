from pg_extensions import *


def start():
    pass


def update():
    window = get_window()
    window.clear() # Choose a color (default is black)

    # Your code comes here

    set_window(window)


if __name__ == "__main__":
    run(start, update)
