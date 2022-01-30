import pygame as pg
from os import path
import sys
from set import *
from food import *
from light import *
from snake import *
from button import *
from images import *
from checkbox import *
from multiplier import *

FPS = 30

# Создаем игру и окно
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()



font_name = pg.font.match_font('arial')
def draw_text(surf, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def SettingLoop():
    Snake.initialize(snake_material)
    MirrorMode = CheckBox(checkmark, highlited_checkbox, highlited_mark, (435, 145), (70, 70))
    StartGame = Button((248, 501), (165, 58), lambda: True, highlited_start)
    ClickEffect = Light()

    pos = (0, 0)
    fl = False
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        was_click = False
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                ClickEffect.add(pg.mouse.get_pos(), click_lights)
                was_click = True
        pos = pg.mouse.get_pos()

        # Обновление
        MirrorMode.update(was_click, pos)
        if StartGame.update(was_click, pos):
            GameLoop(MirrorMode.get_state())
            was_click = False
            ClickEffect.stop_all()
        ClickEffect.update()
        # Рендеринг
        screen.fill(BLACK)
        screen.blit(set_screen, (0, 0))
        MirrorMode.draw(screen)
        StartGame.draw(screen)
        ClickEffect.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pg.display.flip()


def GameLoop(is_mirrored):
    Player = Snake(6, 'player', is_mirrored, snake_material)
    Feed = Food()
    Multy = Multiplier(multiplier_img)
    ClickEffect = Light()
    vector = (0, -1)

    advert_rect = pause_img.get_rect(center=(WIDTH//2, HEIGHT//2))

    SettingBut = Button((395, 517), (233, 67), lambda: True, selected_settings)

    # Цикл игры
    running = True
    paused = False
    lost = False
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        was_click = False
        pos = 0, 0
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                running = False
                sys.exit()
            elif event.type == pg.KEYDOWN:
                key = event.key
                paused = False
                if key == pg.K_q:
                    return
                if lost and key == 13:
                    Player = Snake(6, 'player', is_mirrored, snake_material)
                    Feed = Food()
                    Multy = Multiplier(multiplier_img)
                    vector = (0, -1)
                    lost = False
                if key in moves:
                    new = moves[key]
                    if Player.check_possible_move(new):
                        vector = new
                elif key == 27:
                    paused = True
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                ClickEffect.add(pg.mouse.get_pos(), click_lights)
                was_click = True
        pos = pg.mouse.get_pos()


        # Обновление
        if not paused and not lost:
            Player.update(vector)
            Feed.update(Player, Multy)
            Multy.update(Player, ClickEffect)
        ClickEffect.update()

        if Player.check_for_loose():
            lost = True

        # Рендеринг
        screen.fill(BLACK)


        draw_text(screen, f'Score: {Player.get_score()}', 26, 60, 14, YELLOW)
        draw_text(screen, f'x{Multy.get_multiplier()}', 26, 600, 14, YELLOW)
        Player.draw(screen)
        Feed.draw(screen)
        Multy.draw(screen)

        if paused:
            screen.blit(pause_img, advert_rect)
            if SettingBut.update(was_click, pos):
                ClickEffect.stop()
                return
            SettingBut.draw(screen)
        if lost:
            screen.fill(BLACK)
            screen.blit(end_img, advert_rect)
            if SettingBut.update(was_click, pos):
                return
            SettingBut.draw(screen)

        ClickEffect.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pg.display.flip()

SettingLoop()
pg.quit()
