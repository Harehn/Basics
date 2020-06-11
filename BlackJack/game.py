from BlackJack.deckOfCards import Deck


class Player:
    def __init__(self, name, game=None):
        self.name = name
        self.decision_maker = (lambda: self.hit if input("Type \'h\' to hit and nothing to hold") == "h" else self.hold)
        self.cards = []
        self.game = game
        self.held = False
        self.otherPlayer = None

    def hold(self):
        self.held = True
        return "{} held his turn".format(self.name)

    def hit(self):
        if self.held:
            return None
        else:
            c = self.game.draw()
            self.cards.append(self.game.draw())
        return "{} drew a card : {}".format(self.name, str(c))

    def takeAction(self):
        action = self.decision_maker()
        return action()

    def eval_hand(self):
        aces = 0
        hand = 0
        for card in self.cards:
            if card.number == 1:
                aces += 1
            else:
                number = card.number if card.number < 10 else 10
                hand += number

        for aces in range(aces):
            if hand <= 21:
                hand += 1
            else:
                hand += 10
        return hand

    def isBust(self):
        return self.eval_hand() > 21

    def currentSituation(self):
        return "{} has {} in hand. Total = {}".format(self.name, ",".join([str(c) for c in self.cards]),
                                                      self.eval_hand())

    def reset(self):
        self.cards = []
        self.held = False


class Human(Player):
    def __init__(self, game=None):
        name = input("Enter your name")
        super().__init__(name, game)
        self.decision_maker = self.decision_make()

    def decision_make(self):
        return lambda: self.hit if input("Type \'h\' to hit and nothing to hold") == "h" else self.hold


class CPU(Player):
    def __init__(self, game=None):
        import random
        name = "CPU" + str(random.randint(0, 100))
        super().__init__(name, game)
        self.decision_maker = self.decision_make()

    def decision_make(self):
        import random
        return lambda: random.choice([self.hit, self.hold])


class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.setDefaultPlayers()
        self.deck = Deck().shuffle()
        self.records
        self.verbose = False
        self.printing = False

    def makeNewGame(self):
        return input("Continue(y/n)").lower() == "y"

    def setPlayer1(self, player):
        if player.__class__ == Human:
            self.verbose = True
        player.game = self
        self.player1 = player
        self.resetWinners()

    def setPlayer2(self, player):
        player.game = self
        self.player2 = player
        self.resetWinners()

    def setDefaultPlayers(self):
        self.setPlayer1(CPU())
        self.setPlayer2(CPU())
        self.resetWinners()

    def start(self):
        self.introduce()
        self.next_move()

    def next_move(self):
        if self.deck.isEmpty():
            self.gameEnd()
            return
        if self.player1.held and self.player2.held:
            self.gameEnd()
            return
        if self.player1.isBust() or self.player2.isBust():
            self.gameEnd()
            return
        if self.player1.held:
            self.player1, self.player2 = self.player2, self.player1
        self.printv(self.player1.takeAction())
        self.player1, self.player2 = self.player2, self.player1
        self.printv("", self.player1.currentSituation(), "\n", self.player2.currentSituation(), "\n\n")
        self.next_move()

    def evaluateWinner(self):
        if self.player2.isBust():
            return self.player1
        if self.player1.isBust():
            return self.player2
        if self.player1.eval_hand() == self.player2.eval_hand():
            return None
        elif self.player1.eval_hand() > self.player2.eval_hand():
            return self.player1
        else:
            return self.player2

    def updateWinner(self, winner):
        playername = winner.name if winner else "Draw"
        self.records[playername] = self.records[playername] + 1

    def printWinner(self, winner):
        if self.printing:
            print("", self.player1.currentSituation(), "\n", self.player2.currentSituation())
            print("{} won!!".format(winner.name) if winner else "It's a draw")

    def gameEnd(self):
        winner = self.evaluateWinner()
        self.updateWinner(winner)
        self.printWinner(winner)
        if self.deck.isEmpty():
            self.deck = Deck().shuffle()
        self.player1.reset()
        self.player2.reset()
        # if self.verbose:
        #     self.start()

    def printv(self, *args, **kwargs):
        if self.verbose:
            print(*args, **kwargs)

    def draw(self):
        return self.deck.draw()

    def playGames(self, n):
        for i in range(n):
            self.start()

    def resetWinners(self):
        p1name = self.player1.name if self.player1 else None
        p2name = self.player2.name if self.player2 else None
        self.records = {"Draw": 0, p1name: 0, p2name: 0}

    def introduce(self):
        self.player1.otherPlayer = self.player2
        self.player2.otherPlayer = self.player1
