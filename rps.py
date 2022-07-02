import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class random_player(player):
    def move(self):
        return random.choice(self.moves)


class reflect_player(player):
    def move(self):
        return self.their_move


class cycle_player(player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[2]
        elif self.my_move == self.moves[1]:
            return self.moves[0]
        else:
            return self.moves[1]


class human_player(player):
    def move(self):
        while True:
            move_human = input("Rock, paper, or scissors?\n")
            if move_human.lower() in self.moves:
                return move_human.lower()
            elif move_human.lower() == 'exit':
                exit()


class game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def rounds(self):
        while True:
            self.number_rounds = input(
                "How many rounds would you like to play?\n")
            if self.number_rounds.isdigit():
                return self.number_rounds
            elif self.number_rounds.lower() == 'exit':
                exit()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = "Player 1 wins! Congratulations!"
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_2 = self.score_p2
            winner = "It's a tie."
        else:
            self.score_p2 += 1
            winner = "Player 2 wins! Congratulations!"
        print(
            f"\n\nYou threw: {move1}"
            f"\nYour opponent threw: {move2}"
            f"\n{winner}"
            f"\nScore: Player 1 ({self.score_p1}), "
            f"Player 2 ({self.score_p2})"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(
            "\nGet ready for an exciting "
            "game of rock, paper, scissors!\n"
            "\nIf you would like to quit the game, "
            "please enter \'exit\'."
        )
        self.rounds()
        for round in range(int(self.number_rounds)):
            print(f"\nRound {round + 1}")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print(
                f"\nIt\'s a tie!"
                f"\nScore: Player 1 ({self.score_p1}), "
                f"Player 2 ({self.score_p2})"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\nPlayer 1 wins!"
                f"\nScore: Player 1 ({self.score_p1}), "
                f"Player 2 ({self.score_p2})"
            )
        else:
            print(
                f"\nPlayer 2 wins!"
                f"\nScore: Player 1 ({self.score_p1}), "
                f"Player 2 ({self.score_p2})"
            )


if __name__ == '__main__':
    game = game(human_player(), random.choice(
        [random_player(), reflect_player(), cycle_player()]))
    game.play_game()

print("\nThanks for playing!")