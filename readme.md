How to use:
1. Copy this repository to your python packages location
1.1 By default it is: C:\users\name\AppData\Local\Programs\Python\Python312\Lib\
1.2 Doesnt have to be Python 3.12 to work.
2. Make a new script anywhere you want and import pg_extensions or from pg_extensions import *
3. Make a start() and update() function
4. If __name__ == "__main__": run(start, update) -----> this is to start the program and run the start() and update() functions
5. The run function has other parameters to change the resolution, fullscreen, and other stuff
6. To access the surface, use get_window()
7. If you end up accessing the surface, don't forget to call set_window(window) to make sure the changes you made apply (window.running = False,...)
7. Enjoy