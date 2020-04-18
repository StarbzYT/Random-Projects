print("rock...")
print("paper...")
print("scissors...")
# ask for user input
player1 = input("Player 1, make your move!: ").lower()  # input is case insensitive
print("*** NO CHEATING ***\n\n" * 20)  # this is so that player2 can't see player1's move
player2 = input("Player 2, make your move!: ").lower()
# create all outcomes
if player1 and player2:  # checks to see if player 1 and 2 enter something instead of hitting return
    if player1 == "rock" and player2 == "scissors":  # both of these conditionals must be true for it continue
        print("Player 1 wins!")
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins!")
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    elif player1 == player2:  # both users enter the same move
        print("Its a tie!")
    else:
        print("something went wrong...")  # if the either user does not enter a valid move ie.("sdbsdk")
else:
    print("Someone didn't make a move!")  # this is if the first conditional is false (if the users did not enter anything)



