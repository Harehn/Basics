from BlackJack.game import *


class simpleAI(Player):
    def __init__(self, game=None):
        import random
        name = "simpleAI" + str(random.randint(0, 100))
        super().__init__(name, game)
        self.decision_maker = self.decision_make
        self.deck = trackingDeck()

    def decision_make(self):
        self.deck = trackingDeck()
        self.deck.removeCards(self.cards)
        self.deck.removeCards(self.otherPlayer.cards)
        # print(self.deck.meanVal(), self.eval_hand())
        if self.deck.meanVal() < (21 - self.eval_hand()):
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


