import pygame as pg

class Button():
    def __init__(self, coords, size, func, highlited):
        self.rect = pg.Rect(coords + size)
        self.function = func
        self.highlited_img = highlited
        self.highlited = False
        self.highlited_rect = self.highlited_img.get_rect(midtop=self.rect.midtop)
        self.highlited_rect.center = self.rect.center
    def update(self, was_click, pos, *args):
        if was_click and self.rect.collidepoint(pos):
            return self.function(*args)
        elif self.rect.collidepoint(pos):
            self.highlited = True
        else:
            self.highlited = False
    def draw(self, surf):
        if self.highlited:
            surf.blit(self.highlited_img, self.highlited_rect)
