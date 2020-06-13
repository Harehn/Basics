import random

from BlackJack.AI import SimpleAI
from BlackJack.game import Game


class Specimen():
    ValueOfDraws = 0.7
    NumberOfGames = 1000
    MutationChance = 0.2  # percentage
    MutationAmount = (-8, 8)

    def __init__(self, player):
        self.obj = player
        self.fitness = 0
        # self.fitnessfunc()

    def fitnessfunc(self):
        g = Game()
        g.setPlayer1(self.obj)
        g.playGames(self.NumberOfGames)
        r = g.records
        self.fitness = self.ValueOfDraws * r["Draw"]
        self.fitness += r[self.obj.name]
        self.fitness /= self.NumberOfGames

    def mutate(self):
        if random.random() < self.MutationChance:
            self.obj.confidence += random.randint(*self.MutationAmount)


class Population():
    PopulationSize = 100
    StartingRange = (-200, 200)
    CrossOverRange = 7

    def __init__(self):
        self.specimens = [Specimen(SimpleAI(random.randint(*self.StartingRange), "Best Gen ")) for i in range(100)]
        self.best1 = Specimen(SimpleAI())
        self.best2 = Specimen(SimpleAI())
        self.fit = False
        self.gen = 0

    def breed(self):
        b1 = self.best1.obj.confidence
        b2 = self.best2.obj.confidence
        if b1 > b2:
            b1, b2 = b2, b1
        b1, b2 = b1 - 7, b2 + 7
        if b1 == b2:
            b1 = b1 - 1
            b2 = b2 + 1
        self.specimens = [Specimen(SimpleAI(random.randint(b1, b2), "Best Gen ")) for i in range(100)]  # Crossover
        for s in self.specimens:
            s.mutate()
        self.fit = False

    def fitfun(self):
        if not self.fit:
            for s in self.specimens:
                s.fitnessfunc()

    def getBest(self):
        self.fitfun()
        self.specimens = sorted(self.specimens, key=lambda x: x.fitness, reverse=True)
        return self.specimens[0], self.specimens[1]

    def nextgen(self):
        self.best1, self.best2 = self.getBest()
        ss = self.specimens
        self.breed()
        return ss

    def __str__(self):
        return str([(e.obj.name, e.fitness) for e in self.specimens])


p = Population()
p.fitfun()
# print([(i.obj.name, i.fitness) for i in p.getBest()])
for i in range(10):
    best = p.best1
    best = best.obj.confidence, best.fitness
    #print("Best is", best, [(i.obj.name, i.obj.confidence, i.fitness) for i in p.nextgen()])
    p.nextgen()

g = Game()
g.verbose = True
g.printing = True
g.setPlayer1(p.best1.obj)
g.setPlayer2(SimpleAI())
print(g.player1, g.player2)
g.playGames(100)
print(g.records)
