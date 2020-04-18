# import random to get random numbers from 1 - 10
import random
rand_num = random.randint(1, 10)  # will generate random ints
# ask for user input
# while True means that the while loop will run because it is True (bool), so it will always run until it reaches the break 
while True:
    guess = int(input("pick a number from 1 to 10: "))
    if guess > rand_num:  # guess greater than random int
        print("TOO HIGH!")
    elif guess < rand_num:  # guess less than random int
        print("TOO LOW!")
    else:
        print("YOU GOT IT!")  # only other possible outcome is if they get the random int
        play_again = input("Do you want to play again? (y/n): ").lower()  # case insensitive
        if play_again == "y":
            rand_num = random.randint(1, 10)  # generates random ints again for another game
            guess = None  # reset guess to none
        else:  # if they say "n", the print statement below executes
            print("Thanks for playing!")
            break  # then breaks out of loop to end game





