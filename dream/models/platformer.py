from ..config import *
from .base import BaseModel


class Player(BaseModel):
    MAX_JUMPS = 2
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_ground = True
        self.jumps = 0
        self.direction = 0

    def update(self, dt, gravity=200):
        keys = pg.key.get_pressed()
        left = keys[pg.K_LEFT] or keys[pg.K_a]
        right = keys[pg.K_RIGHT] or keys[pg.K_d]
        up = pg.key.get_just_pressed()[pg.K_UP] or pg.key.get_just_pressed()[pg.K_w] or pg.key.get_just_pressed()[pg.K_SPACE]
        down = keys[pg.K_DOWN] or keys[pg.K_s]

        def jump():
            if self.jumps < self.MAX_JUMPS or self.on_ground:
                self.vel.y = -300
                self.jumps += 1
                self.on_ground = False

        if left:
            self.vel.x = -self.speed

        if right:
            self.vel.x = self.speed

        if not (right or left):
            self.vel.x = 0

        if up:
            jump()

        if not self.on_ground:
            self.vel.y += gravity * dt

        else:
            self.jumps = 0
            self.vel.y = 0

        if self.pos.x < 101 and self.vel.x < 0:
            self.pos.x = 100
            self.vel.x = 0

        if self.pos.x > self.screen.get_width() - 100 and self.vel.x > 0:
            self.pos.x = self.screen.get_width() - 100

        self.pos += self.vel * dt
        self.rect.center = self.pos

        if self.rect.bottom > self.screen.get_rect().bottom:
            self.on_ground = True
            self.pos.y -= 1
