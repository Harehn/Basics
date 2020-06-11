from BlackJack.AI import simpleAI
from BlackJack.game import Game

g = Game()
g.setPlayer1(simpleAI())
g.playGames(10000)
print(g.records)
