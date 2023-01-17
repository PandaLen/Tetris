import pygame as pg
import sys
from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        
        self.running = True
    
    def update(self):
        self.clock.tick(FPS)
    
    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        pg.display.flip()
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()