from ..config import *
from .base import BaseModel

class Player(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def update(self, dt):
        keys = pg.key.get_pressed()
        self.vel = pg.Vector2(0, 0)
        
        if keys[pg.K_LEFT]:
            self.vel.x = -self.speed
        if keys[pg.K_RIGHT]:
            self.vel.x = self.speed
        if keys[pg.K_UP]:
            self.vel.y = -self.speed
        if keys[pg.K_DOWN]:
            self.vel.y = self.speed

        self.pos += self.vel * dt
        self.rect.center = self.pos

