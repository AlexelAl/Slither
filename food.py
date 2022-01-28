import pygame as pg
import random
from set import *

class Food():
    def __init__(self):
        self.image = pg.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.new_food()

    def new_food(self):
        self.rect.topleft = self.make_new_coord()
        self.cell_pos = self.rect.topleft[0] // CELL_SIZE, self.rect.topleft[1] // CELL_SIZE

    def make_new_coord(self):
        x = random.randint(0, WIDTH//CELL_SIZE - 1)
        y = random.randint(0, HEIGHT//CELL_SIZE - 1)
        return x * CELL_SIZE, y * CELL_SIZE

    def update(self, snake_obj, multiplier_obj):
        if self.cell_pos in snake_obj.get_body():
             self.new_food()
             snake_obj.eat_food(multiplier_obj.get_multiplier())
    def draw(self, surf):
        surf.blit(self.image, self.rect)
