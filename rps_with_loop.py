from random import randint  # must import randint to create the computer player
# both scores are originally set to zero
player_wins = 0
computer_wins = 0
# print("rock...")
# print("paper...")
# print("scissors...")
# create AI & ask for user input
# use while loop to continue loops until someone gets 2 wins
while player_wins < 2 and computer_wins < 2:  # either player's wins must be less than zero
    print(f"Player score: {player_wins} Computer score: {computer_wins}")
    player = input("Player, make your move: ").lower()  #case insensitive
    if player == "quit" or player == "q":  # if the player enters q or quit,the loop breaks and reports the scores
        break
    rand_num = randint(0, 2)  # each int is assigned to a move for the computer
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"The computer played {computer}!")  # report what the computer played
    # create all outcomes
    # if player: basically means that the user must enter some string in order for the rest of the code to run
    if player:
        if player == computer:  # declare tie first so we can use else statements later (if the outcome is not a tie only then the other code will execute)
            print("Its a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Player wins!")
                player_wins += 1  # add a win to the variable player_wins
            else:  # instead of creating another outcome, the computer will win in this case because it can only play paper if not scissors (it can't be a tie!)
                print("Computer wins!")
                computer_wins += 1  # add a win to the variable computer_wins
        elif player == "scissors":
            if computer == "rock":
                print("Computer wins!")
                computer_wins += 1
            else:
                print("Player wins!")
                player_wins += 1
        elif player == "paper":
            if computer == "scissors":
                print("Computer wins!")
                computer_wins += 1
            else:
                print("Player wins!")
                player_wins += 1
    # if user writes giberish, the else statement below executes
        else:
            print("Please enter a valid move...")
    # if user does not make their move and instead hit enter, the else statement below executes
    else:
        print("You didn't make a move!")
# instead of ending the loop witout saying anything, we can report the final scores
print(f"FINAL SCORES... Player score: {player_wins} Computer score: {computer_wins}")
# create conditionals for each outcome
if player_wins > computer_wins:
    print("PLAYER IS THE WINNER!")
elif player_wins == computer_wins:
    print("IT IS A TIE!")
else:
    print("THE COMPUTER IS THE WINNER!")

