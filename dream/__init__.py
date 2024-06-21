from .config import *


class Manger:
    def __init__(self):
        self.menus:list[Menu] = []
        self.current:list[Menu] | None = None
        self.running = True
        self.main: Menu | None = None

    def add_menu(self, menu, main:bool=False):
        self.menus.append(menu)
        if main:
            self.main = menu
        elif not self.main:
            self.current = menu
        if self.main:
            self.current = self.main

    def run(self):
        if len(self.menus) == 0:
            raise Exception("No menus added")
        while self.running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
            self.current.update(events)

        pg.quit()
        sys.exit(0)

    def switch(self, menu):
        self.current = menu


class Menu:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.dt = 0
        self.sprites = pg.sprite.Group()
        self.players = pg.sprite.Group()

    def add_sprite(self, sprite):
        self.sprites.add(sprite)

    def add_player(self, player):
        self.players.add(player)

    def update(self, events):
        self.dt = self.clock.tick(60) / 1000

        self.screen.fill("white")
        self.players.update(self.dt)
        self.players.draw(self.screen)
        self.sprites.update(self.dt)
        self.sprites.draw(self.screen)

        pg.display.flip()