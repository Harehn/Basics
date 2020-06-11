class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        s = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
        self.value = s[number - 1]

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self, cards=[]):
        self.cards = cards
        if len(self.cards) == 0:
            suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
            for suit in suits:
                for num in range(1, 14):
                    self.cards.append(Card(suit, num))

    def __str__(self):
        return "\n".join([str(i) for i in self.cards])

    def shuffle(self):
        import random
        random.shuffle(self.cards)
        return Deck(self.cards)

    def get_generator(self):
        return (i for i in self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        ret = self.cards[0]
        self.cards = self.cards[1:]
        return ret

    def isEmpty(self):
        return len(self.cards) == 0

#
# d = Deck().shuffle()
# while input("Draw? (y/n)").lower() == "y":
#     print(d.draw())

