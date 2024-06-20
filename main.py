import dream as eg
from dream.models.RPG import Player


world = eg.Engine()

player = Player(world.screen)
world.add_sprite(player)
world.run()
