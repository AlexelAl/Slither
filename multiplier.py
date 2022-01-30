import pygame as pg
from set import *
from images import click_lights
import random

class Multiplier():
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.cell_pos = 0, 0
        self.pos = 0, 0
        self.multy = 1
        self.in_field = False
    def get_multiplier(self):
        return self.multy

    def make_new_coord(self):
        x = random.randint(0, WIDTH//CELL_SIZE - 1)
        y = random.randint(0, HEIGHT//CELL_SIZE - 1)
        return x * CELL_SIZE, y * CELL_SIZE

    def update(self, snake_obj, effect_obj):
        if self.in_field and self.cell_pos in snake_obj.get_body():
            self.multy += 2
            if self.multy == 3:
                self.multy = 2
            self.in_field = False
        elif not self.in_field:
            chance = random.randint(0, 2500)
            if chance == 2499:
                self.in_field = True
                self.pos = self.make_new_coord()
                self.cell_pos = self.pos[0] // CELL_SIZE, self.pos[1] // CELL_SIZE
                self.rect.center = self.pos[0] + CELL_SIZE // 2, self.pos[1] + CELL_SIZE // 2
                effect_obj.add(self.rect.center, click_lights)
    def draw(self, surf):
        if self.in_field:
            surf.blit(self.image, self.rect)
