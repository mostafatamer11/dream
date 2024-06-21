from ..config import *


class BaseModel(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, speed:int=100, color:Tuple[int, int, int]|str="blue"):
        self.screen = screen
        super().__init__()
        self.image = pg.Surface((30, 40))
        self.image.fill(color)
        self.pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.rect = self.image.get_rect(center=self.pos)
        self.vel = pg.Vector2(0, 0)
        self.speed = speed
        self.mask = pg.mask.from_surface(self.image)

    def load_image(self, path:str):
        self.image = pg.image.load(path)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pg.mask.from_surface(self.image)
