from random import randint  # import the random module to use randint
# heads or tails game


class Game:
    def _heads_tails(self):  # make a heads or tails method that randomly chooses a move
        rand_num = randint(0, 1)
        if rand_num == 0:
            move = "Heads"
        else:
            move = "Tails"
        return move

    def play_game(self):  # play game and make a move!
        actual_move = self._heads_tails().lower()
        make_move = input("Heads or Tails?:\n").lower()
        if make_move:  # if the user enters something truthy, the code below runs
            if make_move == actual_move:
                print(f"You were right! It was {actual_move}!")
            elif (make_move.lower() == "tails" and actual_move.lower() == "heads") or (make_move.lower() == "heads" and actual_move.lower() == "tails"):
                print(f"NOPE! It was {actual_move}!")
            else:
                print(f"{make_move} is not a valid move...")  # runs if input isn't heads or tails
        else:  # if user input was falsy, this runs
            print(f"You didn't make a move!")

    def toss_coins(self):  # toss any number odf coins and check how many are heads or tails
        num_of_coins = int(input("How many coins would you like to toss?\n"))
        # try to toss the coins and compare ints
        count = 0  # keep count of how many tosses there are
        moves = []  # append to this list full of moves
        while count < num_of_coins:
            # keep track of the num of heads/tails
            heads = 0
            tails = 0
            move = self._heads_tails().lower()
            moves.append(move)
            # check and compare the move
            for move in moves:  # check moves list to see heads/tails
                if move.lower() == "heads":
                    heads += 1  # increment heads if heads
                else:
                    tails += 1  # increment tails if tails
            count += 1  # add one cycle to count
        print(f"Out of {num_of_coins}, {heads} were heads and {tails} were tails!")  # states the stats


new_game = Game()
new_game.play_game()
new_game.toss_coins()




