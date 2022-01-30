import pygame as pg
from set import *
from os import path
from images import *

material_matrix = []

class Snake():
    def __init__(self, lenth, type, mode, material,
                coord=(WIDTH//CELL_SIZE//2, HEIGHT//CELL_SIZE//2)):
        self.start_lenth = lenth

        self.head = pg.Surface((CELL_SIZE, CELL_SIZE))
        self.head.fill(WHITE)

        self.material = material
        self.material = pg.transform.scale(self.material, (WIDTH, HEIGHT))

        self.body = [coord] * lenth
        self.image = pg.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.is_mirror = mode
    def get_score(self):
        return len(self.body) - self.start_lenth

    def get_body(self):
        return self.body

    def check_for_loose(self):
        x, y = self.body[0]
        if self.body.count((x, y)) > 1:
            return True
        if not self.is_mirror and\
            not(0 <= x < WIDTH//CELL_SIZE and 0 <= y < HEIGHT//CELL_SIZE):
                return True
        return False

    def check_possible_move(self, new_vector):
        new_x, new_y = new_vector
        if (self.body[0][0] + new_x, self.body[0][1] + new_y) == self.body[1]:
            return False
        else:
            return True

    def eat_food(self, multy):
        self.body.extend([self.body[-1]] * multy)

    def update(self, vector):
        for i in range(1, len(self.body)):
            self.body[-i] = self.body[-(i + 1)]
        self.body[0] = self.body[0][0] + vector[0], self.body[0][1] + vector[1]
        if self.is_mirror:
            x, y = self.body[0]
            x, y = x % (WIDTH // CELL_SIZE), y % (HEIGHT // CELL_SIZE)
            self.body[0] = x, y
    def draw(self, surf):
        last = self.body[0]
        for i in self.body:
            curr_coord = i[0] * CELL_SIZE, i[1] * CELL_SIZE
            self.rect.topleft = curr_coord
            if i[0] < 66 and i[1] < 66:
                surf.blit(material_matrix[i[0]][i[1]], self.rect)
                if i == self.body[0]:
                    surf.blit(self.head, self.rect)
            if i == last and i != self.body[0]:
                break
            last = i


    def initialize(material):
        global material_matrix
        material_matrix = [[] for i in range(66)]

        for i in range(66):
            for j in range(66):
                material_matrix[i].append(material.subsurface((j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
