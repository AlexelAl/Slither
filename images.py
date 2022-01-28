from os import path
from set import *
import pygame as pg

img_dir = path.join(path.dirname(__file__), 'img')
light_dir = path.join(img_dir, 'lights')


#  Game Loop images
pause_img = pg.image.load(path.join(img_dir, "pause.jpeg"))
pause_img.set_colorkey(BLACK)

end_img = pg.image.load(path.join(img_dir, "end.jpeg"))

selected_settings = pg.image.load(path.join(img_dir, "selected_settings.png"))

multiplier_img = pg.image.load(path.join(img_dir, "doubler.png"))
multiplier_img.set_colorkey(BLACK)

snake_material = pg.image.load(path.join(img_dir, "snake_material2.png"))
snake_material = pg.transform.scale(snake_material, (WIDTH, HEIGHT))


# Setting Screen images
set_screen = pg.image.load(path.join(img_dir, "settings.png"))

checkmark = pg.image.load(path.join(img_dir, "mark.png"))
checkmark.set_colorkey(BLACK)

highlited_mark = pg.image.load(path.join(img_dir, "chackmark.png"))

highlited_start = pg.image.load(path.join(img_dir, "selected_start.png"))
highlited_start.set_colorkey(RED)

highlited_checkbox = pg.image.load(path.join(img_dir, "selected_checkbox.png"))
highlited_checkbox.set_colorkey(YELLOW)

# global images

click_lights = [pg.image.load(path.join(light_dir, f'Light{i}.png')) for i in range(11)]
