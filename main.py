#!/usr/bin/env python
"""
Based on pg.examples.stars from Pygame
"""
import random
import math
import pygame as pg

from typing import List, Tuple

# constants
WINSIZE = [640, 480]


class Shape:
    def draw(self, screen: pg.Surface):
        pass

class Rectangle:
    def __init__(self, c1: Tuple[int, int], c2: Tuple[int, int]):
        self.c1 = c1
        self.c2 = c2

    def draw(self, screen: pg.Surface, color: Tuple[int, int, int]):
        left = min(self.c1[0], self.c2[0])
        top = min(self.c1[1], self.c2[1])
        width = max(self.c1[0], self.c2[0]) - left
        height = max(self.c1[1], self.c2[1]) - top
        pg.draw.rect(screen, color, pg.Rect(left, top, width, height), width=1)

def draw_shapes(screen: pg.Surface, shapes: List[Shape], color):
    for shape in shapes:
        shape.draw(screen, color)

def main():
    # initialize and prepare screen
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("pygame Canvas Example")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(white)

    clock = pg.time.Clock()

    # main game loop
    done = 0
    shapes = []
    rubber_band = None
    while not done:
        draw_shapes(screen, shapes, white)
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = 1
                break
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                if rubber_band is not None:
                    rubber_band is None
                rubber_band = Rectangle(tuple(e.pos), tuple(e.pos))
                shapes.append(rubber_band)
            elif e.type == pg.MOUSEMOTION:
                if rubber_band is not None:
                    rubber_band.c2 = tuple(e.pos)
            elif e.type == pg.MOUSEBUTTONUP and e.button == 1:
                rubber_band = None
        clock.tick(100)
        draw_shapes(screen, shapes, black)
        pg.display.update()
        
    pg.quit()

if __name__ == "__main__":
    main()
