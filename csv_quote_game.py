# quotes guessing game
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"  # base url that will be attached with url


def read_quotes(filename):  # read the quotes.csv file and store everything in a list
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def play_game(data):
    quote = choice(data)  # randomly chooses a quote along with the author name and bio link
    remaining_guesses = 4
    print("Here's a quote:")
    print(f"{quote['quote']}")
    guess = ""  # originally, guess is an empty string to run the while loop

    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:  # this runs as long as the user doesn't guess the author or the remaining_guesses is greater than 0
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")

        if guess.lower() == "q" or guess.lower() == "quit":  # user can quit anytime
            print(f"The answer was {quote['author']}...")
            break

        elif guess.lower() == quote["author"].lower():
            print(f"YES YOU ARE CORRECT! IT WAS INDEED {quote['author'].upper()}!")
            break
        remaining_guesses -= 1  # decrements everytime the loop starts over. It means that the user still guessed incorrect

        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['Bio-Link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: This is their date of birth and birth place: {birth_date}, {birth_place}.")

        elif remaining_guesses == 2:
            num_letters = len(soup.find(class_="author-title").get_text().replace(" ", ""))
            print(f"Not quite. Here is another hint: There are {num_letters} letters in their name!")

        elif remaining_guesses == 1:
            name = soup.find(class_="author-title").get_text()
            print(f"This is your last hint! The first letter in their name is {name[0]}!")

        else:
            print(f"Sorry you were wrong! The answer was {quote['author']}!")

    again = ""
    while again.lower() not in ("y", "n", "no", "yes"):
        again = input("Would you like to play again? (y/n): ")

    if again.lower() in ("y", "yes"):
        print("Okay! You will play again!")
        return play_game(data)

    else:
        print("Thanks for playing!")


quotes = read_quotes("quotes.csv")  # call first to use data into the csv file "quotes.csv"
play_game(quotes)  # then play the game!



