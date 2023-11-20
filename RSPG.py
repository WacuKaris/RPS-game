#!/usr/bin/env python3
import random

moves = ["rock", "paper", "scissors"]


class Player:
    def __init__(self):
        self.score = 0
        self.my_last_move = None
        self.their_last_move = None

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            player_input = input("WELCOME! Choose a move!"
                                 "rock, paper, or scissors: ").lower()
            if player_input in moves:
                return player_input
            else:
                print("Sorry that is not a valid input!"
                      "Please insert a valid option!")


class ReflectPlayer(Player):
    def move(self):
        if self.their_last_move:
            return self.their_last_move
        return random.choice(moves)


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.round_number = 0

    def move(self):
        self.round_number += 1
        if self.round_number <= len(moves):
            return moves[self.round_number - 1]
        else:
            # Calculate the index of the next move using modulus
            current_index = self.round_number - 1
            next_index = (current_index - len(moves) + 1) % len(moves)
            return moves[next_index]


def beats(move1, move2):
    if (move1 == "rock" and move2 == "scissors") or \
       (move1 == "scissors" and move2 == "paper") or \
       (move1 == "paper" and move2 == "rock"):
        return True
    return False


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1 plays: ", end='')
        self.print_colored(move1)
        print(f"Player 2 plays: ", end='')
        self.print_colored(move2)

        if move1 == move2:
            print("\n\033[96mIt is a tie!\033[0m")
        elif beats(move1, move2):
            print("\n\033[93mPlayer 1 wins this round!\033[0m")
            self.player1.score += 1
        else:
            print("\n\033[92mPlayer 2 wins this round!\033[0m")
            self.player2.score += 1

        # Display scores after each round
        print(f"Player 1 score: {self.player1.score}")
        print(f"Player 2 score: {self.player2.score}")

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def print_colored(self, move):
        if move == 'rock':
            print("\033[36m" + move + "\033[0m", end=' ')
        elif move == 'paper':
            print("\033[95m" + move + "\033[0m", end=' ')
        elif move == 'scissors':
            print("\033[91m" + move + "\033[0m", end=' ')

    def play_game(self, rounds=3):
        print("Game start!")
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over! Final score:")
        print(f"Player 1 score: {self.player1.score}")
        print(f"Player 2 score: {self.player2.score}")


if __name__ == '__main__':
    player1 = HumanPlayer()
    player2 = CyclePlayer()
    game = Game(player1, player2)
    game.play_game(3)  # You can specify the number of rounds you want to play
