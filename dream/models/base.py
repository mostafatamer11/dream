from ..config import *


class BaseModel(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self, dt):
        pass

    def render(self):
        pass