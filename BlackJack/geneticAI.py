import random

from BlackJack.AI import SimpleAI
from BlackJack.game import Game


class Specimen():
    ValueOfDraws = 0.5
    NumberOfGames = 100
    MutationChance = 0.2
    MutationAmount = 8
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
            self.obj.confidence += (random.random()*self.MutationAmount)


class Population():
    def __init__(self):
        self.specimens = [Specimen(SimpleAI( float("{:.2f}".format(random.random())) )) for i in range(100)]
        self.best1 = Specimen(SimpleAI())
        self.best2 = Specimen(SimpleAI())
        self.fit = False

    def breed(self):
        b1 = int(self.best1.obj.confidence*1000)
        b2 = int(self.best2.obj.confidence*1000)
        if b1 > b2:
            b1, b2 = b2, b1
        if b1 == b2:
            b1 = b1-1
            b2 = b2+1
        self.specimens = [Specimen(SimpleAI(random.randrange(b1, b2)/1000)) for i in range(100)] #Crossover
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
for i in range(3):
    best = p.best1
    print([(i.obj.name, i.fitness) for i in p.nextgen()], "Best is", best)