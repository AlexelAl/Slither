import pygame as pg

class CheckBox():
    def __init__(self, checkmark, highlited, highlited_mark, coords, size):
        self.rect = pg.Rect(coords + size)

        self.mark = checkmark
        self.mark_rect = self.mark.get_rect(center=self.rect.center)

        self.checked = False

        self.highlited_img = highlited
        self.highlited = False
        self.highlited_rect = self.highlited_img.get_rect(center=self.rect.center)

        self.highlited_mark = highlited_mark
        self.highlited_mark_rect = self.highlited_mark.get_rect(center=self.rect.center)

    def update(self, was_click, pos):
        if was_click and self.rect.collidepoint(pos):
            self.checked = not self.checked
        if self.rect.collidepoint(pos):
            self.highlited = True
        else:
            self.highlited = False

    def draw(self, surf):
        if self.highlited:
            surf.blit(self.highlited_img, self.highlited_rect)
            if self.checked:
                surf.blit(self.highlited_mark, self.highlited_mark_rect)
        elif self.checked:
            surf.blit(self.mark, self.mark_rect)
            
    def get_state(self):
        return self.checked
