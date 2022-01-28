import pygame as pg
from set import *
from os import path

class Light():
    def __init__(self, frames_list, lenth):
        self.frames = frames_list
        self.lenth = lenth
        self.play_coord = 0, 0
        self.curr_frame = 0
        self.play = False
    def update(self, was_click, pos):
        if was_click:
            self.play = True
            self.play_coord = pos
    def draw(self, surf):
        if self.play:
            self.rect = self.frames[self.curr_frame].get_rect(center=self.play_coord)
            self.curr_frame += 1
            surf.blit(self.frames[self.curr_frame], self.rect)
        if self.curr_frame == self.lenth - 1:
            self.curr_frame = 0
            self.play = False
    def forced_call(self, pos):
        self.play = True
        self.curr_frame = 0
        self.play_coord = pos
