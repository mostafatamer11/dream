from ..config import *
from .base import BaseModel

class Player(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = pg.Vector2(0, 0)


    def update(self, dt):
        up, down, left, right = super().update(dt)
        if left:
            self.vel.x = -self.speed
        if right:
            self.vel.x = self.speed
        if up:
            self.vel.y = -self.speed
        if down:
            self.vel.y = self.speed
            
        if not (left or right):
            self.vel.x = 0
        if not (up or down):
            self.vel.y = 0



