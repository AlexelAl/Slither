import pygame as pg
from set import *
from os import path



class Effect():
    def __init__(self, pos, frames):
        self.pos = pos
        self.frames = frames
        self.lenth = len(frames)
        self.curr_frame = 0
    def update(self):
        self.image = self.frames[self.curr_frame]
        self.rect = self.image.get_rect(center=self.pos)
        self.curr_frame += 1
        if self.curr_frame >= self.lenth:
            return True
    def draw(self, surf):
        surf.blit(self.image, self.rect)




class Light():
    def __init__(self):
        self.effects = []
    def update(self):
        to_del = []
        for i in range(len(self.effects)):
            if self.effects[i].update():
                to_del.append(i)
        for i in range(len(to_del)):
            del self.effects[to_del[i] - i]
    def draw(self, surf):
        for effect in self.effects:
            effect.draw(surf)
    def add(self, pos, frames):
        self.effects.append(Effect(pos, frames))
    def stop_all(self):
        self.effects.clear()
