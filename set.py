from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT
from os import path
WIDTH = 660
HEIGHT = 660

CELL_SIZE = 10

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


moves = {
        K_UP: (0, -1),
        K_DOWN: (0, 1),
        K_RIGHT: (1, 0),
        K_LEFT: (-1, 0)
        }
