from BlackJack.game import *


class simpleAI(Player):
    def __init__(self, game=None):
        import random
        name = "simpleAI" + str(random.randint(0, 100))
        super().__init__(name, game)
        self.decision_maker = self.decision_make()

    def decision_make(self):
        pass
