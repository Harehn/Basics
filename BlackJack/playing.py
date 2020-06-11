from BlackJack.AI import SimpleAI
from BlackJack.game import Game

g = Game()
g.setPlayer1(SimpleAI())
g.playGames(10000)
print(g.records)
