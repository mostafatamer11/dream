import dream as eg
from dream.models.platformer import Player

manger = eg.Manger()
world = eg.Menu()
test = eg.Menu()

player = Player(world.screen)
world.add_player(player)

manger.add_menu(world, True)
manger.add_menu(test)
manger.run()
