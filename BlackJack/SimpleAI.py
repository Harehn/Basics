from BlackJack.game import *


def my_timer(orig_fun):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        output = orig_fun(*args, **kwargs)
        t2 = time.time()
        #print("{} ran in {} seconds".format(orig_fun.__name__, (t2 - t1)))
        return output

    return wrapper


class SimpleAI(Player):
    ConfidenceMultiplier = 0.1 #So that confidence can be an integer

    def __init__(self, confidence=0, name="simpleAI", game=None):
        import random
        name = name + str(random.randint(0, 100))
        super().__init__(name, game)
        self.decision_maker = self.decision_make
        self.deck = trackingDeck()
        self.confidence = confidence

    def decision_make(self):
        self.deck = trackingDeck()
        self.deck.removeCards(self.cards)
        self.deck.removeCards(self.otherPlayer.cards)
        if (self.deck.meanVal() - (self.confidence*self.ConfidenceMultiplier)) < (21 - self.eval_hand()):
            return self.hit
        else:
            return self.hold


class trackingDeck():
    def __init__(self):
        self.deck = {i: (16 if i == 10 else 4) for i in range(1, 11)}

    def meanVal(self):
        num_cards = 0
        totalScore = 0
        for k, v in self.deck.items():
            num_cards += v
            totalScore += (k*v)
        return totalScore // num_cards

    def removeCards(self, cards):
        for c in cards:
            val = c.number if c.number < 10 else 10
            self.deck[val] = self.deck[val] - 1


