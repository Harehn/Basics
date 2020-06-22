from BlackJack.GeneticAlgorithm import Population

from matplotlib import pyplot as plt

# import time
#
# t1 = time.time()
p = Population()
p.fitfun()
p.getBest()
graphs_y = []
graphs_x = list(range(100))

for i in range(10):
    # best = p.best1
    # best = best.obj.confidence, best.fitness
    # print("Best is", best, [(i.obj.name, i.obj.confidence, i.fitness) for i in p.nextgen()])
    graphs_y.append(list(reversed([i.fitness for i in p.nextgen()])))


for i, y in enumerate(graphs_y):
    plt.plot(graphs_x, y, label=("Gen" + str(i+1)))

plt.xkcd()

plt.legend()

plt.xlabel("Population specimens")
plt.ylabel("% Success")
plt.title("BlackJack AI Progression")
# t2 = time.time()
# print("The genetic algorithm took {} seconds".format(t2-t1))
plt.show()

# g = Game()
# g.verbose = True
# g.printing = True
# g.setPlayer1(p.best1.obj)
# g.setPlayer2(SimpleAI())
# print(g.player1, g.player2)
# g.playGames(100)
# print(g.records)
