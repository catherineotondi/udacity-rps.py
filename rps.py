import random

"""This program plays a game of Rock, Paper, Scissors
between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class
for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, first_player_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        self.mvmt = random.choice(moves)
        print(f"Opponent played, {self.mvmt}")
        return self.mvmt

    def learn(self, first_player_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.reflPlayer_move = ""

    def move(self):
        if self.reflPlayer_move == "":
            self.first_player_move = random.choice(moves)
            print(f"The Opponent has played, {self.first_player_move}")
            return self.first_player_move

        else:
            self.the_move = self.reflPlayer_move
            print(f"The Opponent has played, {self.the_move}")
            return self.the_move

    def learn(self, first_player_move):
        self.reflPlayer_move = first_player_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

        self.mvmt = ""

    def move(self):
        if self.mvmt == "":
            self.mvmt = "rock"
            print(f" The Opponent has played, {self.mvmt}")
            return self.mvmt
        if self.mvmt == "rock":
            self.mvmt = "paper"
            print(f"The Opponent has played, {self.mvmt}")
            return self.mvmt
        if self.mvmt == "paper":
            self.mvmt = "scissors"
            print(f"The Opponent has played, {self.mvmt}")
            return self.mvmt
        if self.mvmt == "scissors":
            self.mvmt = "rock"
            print(f"The Opponent has played, {self.mvmt}")
            return self.mvmt


class HumanPlayer(Player):
    def __init__(self):

        super().__init__()

    def move(self):
        while True:
            self.mvmt = input("Rock, paper," "scissors?\n").lower()
            if self.mvmt in moves:
                print(f"You played {self.mvmt}")
                return self.mvmt

    def learn(self, first_player_move):
        pass


class rock_set_player(Player):
    def move(self):
        # it returns rock always
        self.mvmt = "rock"
        print(f" The Opponent has played, {self.mvmt}")
        return self.mvmt


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        first_player_move = self.p1.move()
        second_player_move = self.p2.move()
        self.p1.learn(second_player_move)
        self.p2.learn(first_player_move)

        self.affirmWinner(first_player_move, second_player_move)

    def affirmWinner(self, first_player_move, second_player_move):
        if beats(first_player_move, second_player_move):
            print("## " + player_one_name + ", GOOD JOB!! KEEP GOING ##")
            self.p1.score += 1
            print("CHECK OUT THE SCORES BELOW!")
            print(
                f"""Score: {player_one_name} {self.p1.score},""" +
                f""" {player_two_name} {self.p2.score}"""
            )

        elif beats(second_player_move, first_player_move):
            print("" + player_two_name + ", GOOD JOB!! KEEP GOING!! ")
            self.p2.score += 1
            print("CHECK OUT THE SCORES BELOW!")
            print(
                f"""Score: {player_one_name} {self.p1.score},""" +
                f""" {player_two_name} {self.p2.score}"""
            )

        else:
            print("OOPS!! A DRAW CONDITION !! ")
            print(
                f"""Score: {player_one_name} {self.p1.score},""" +
                f""" {player_two_name} {self.p2.score}"""
            )

    def validateActualwinner(self):
        print("Here comes the FINAL OUTCOME!! ")
        print(f"{player_one_name}: {self.p1.score}\n"
              f"{player_two_name}: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print(player_one_name + ", YOU HAVE WON")
        elif self.p2.score > self.p1.score:
            print(player_two_name + " HAS WON!!")
        else:
            print("DRAW STATUS ADMINISTERED!!")

    def start_end_play(self, game_status):
        print(" *******************")
        print("The FUN " + game_status + " YAY!! ")
        print(" *******************")

    def play_game(self, playing_rounds):
        self.start_end_play("STARTS")
        for round in range(playing_rounds):
            print(f"Round {round + 1}:")
            self.play_round()

        self.validateActualwinner()
        self.start_end_play("ENDS")


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


if __name__ == "__main__":
    oppObj_list = []

    oppObj_list.append(ReflectPlayer())
    oppObj_list.append(rock_set_player())
    oppObj_list.append(RandomPlayer())
    oppObj_list.append(CyclePlayer())

    while True:
        try:
            print("Yoo!! Let's play Rock Paper"
                  "Scissors game. Its gonna be fun")
            player_one_name = input("Kindly input your name\n")
            print("Hello " + player_one_name)
            player_two_name = input(player_one_name +
                                    ", kindly input your opponent's name\n")
            print(player_one_name + ", you are"
                  "playing against " + player_two_name)
            playing_rounds = input("How many playing"
                                   " rounds do you want to partake?\n")
            rounds_int = int(playing_rounds)
            game = Game(HumanPlayer(), random.choice(oppObj_list))
            game.play_game(rounds_int)
            break

        except ValueError:
            print("Input a valid number of playing rounds")
            continue
