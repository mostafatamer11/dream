from .config import *




class Engine:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.dt = 0
        self.sprites = pg.sprite.Group()

    def run(self):
        running = True
        while running:
            self.dt = self.clock.tick(60) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.screen.fill("white")
            self.sprites.update(self.dt)
            self.sprites.draw(self.screen)

            pg.display.flip()

        pg.quit()
        sys.exit(0)

    def add_sprite(self, sprite):
        self.sprites.add(sprite)