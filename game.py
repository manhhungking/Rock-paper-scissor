import threading


class Game:
    def __init__(self, id):
        self.p1_went = False
        self.p2_went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.draws = 0
        self.start = False
        self.updated = False
        # self.lock = threading.Lock()

    def get_player_move(self, player):
        return self.moves[player]

    def play(self, player, move):
        # with self.lock:
        if move == "random":
            return
        self.moves[player] = move
        if player == 0:
            self.p1_went = True
        else:
            self.p2_went = True

    def connected(self):
        return self.ready

    def both_went(self):
        return self.p1_went and self.p2_went

    def winner(self):
        # with self.lock:
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        # calculate which player has won the game based on selected move
        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "P" and p2 == "S":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        if self.updated == False:
            if winner == -1:
                self.draws += 1
            else:
                self.wins[winner] += 1
            self.updated = True
        print(self.wins, self.draws, self.id)
        return winner

    def find_winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        # calculate which player has won the game based on selected move
        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "P" and p2 == "S":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0

        return winner

    def softreset(self):
        self.p1_went = False
        self.p2_went = False
        self.updated = False

    def hardreset(self):
        self.p1_went = False
        self.p2_went = False
        self.moves = [None, None]
        self.wins = [0, 0]
        self.draws = 0

    def check_end(self):
        if self.wins[0] >= 3:
            print("Game ended")
            return 0
        elif self.wins[1] >= 3:
            print("Game ended")
            return 1
        return -1
