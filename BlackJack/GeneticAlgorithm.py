import random

from BlackJack.SimpleAI import SimpleAI
from BlackJack.game import Game
from BlackJack.SimpleAI import my_timer



class Specimen():
    ValueOfDraws = 0.0
    NumberOfGames = 1000
    MutationChance = 0.5  # percentage
    MutationAmount = (-70, 70)

    def __init__(self, player):
        self.obj = player
        self.fitness = 0
        # self.fitnessfunc()

    @my_timer
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
    CrossOverRange = 20

    @my_timer
    def __init__(self):
        self.specimens = [Specimen(SimpleAI(random.randint(*self.StartingRange), "Best Gen ")) for i in range(100)]
        self.best1 = Specimen(SimpleAI())
        self.best2 = Specimen(SimpleAI())
        self.fit = False
        self.gen = 0

    @my_timer
    def breed(self):
        b1 = self.best1.obj.confidence
        b2 = self.best2.obj.confidence
        if b1 > b2:
            b1, b2 = b2, b1
        b1, b2 = b1 - self.CrossOverRange, b2 + self.CrossOverRange
        if b1 == b2:
            b1 = b1 - 1
            b2 = b2 + 1
        self.specimens = [Specimen(SimpleAI(random.randint(b1, b2), "Best Gen ")) for i in range(100)]  # Crossover
        for s in self.specimens:
            s.mutate()
        self.fit = False

    @my_timer
    def fitfun(self):
        if not self.fit:
            for s in self.specimens:
                s.fitnessfunc()

    @my_timer
    def getBest(self):
        self.fitfun()
        self.specimens = sorted(self.specimens, key=lambda x: x.fitness, reverse=True)
        return self.specimens[0], self.specimens[1]

    @my_timer
    def nextgen(self):
        self.best1, self.best2 = self.getBest()
        ss = self.specimens
        self.breed()
        self.gen += 1
        return ss

    def __str__(self):
        return str([(e.obj.name, e.fitness) for e in self.specimens])

