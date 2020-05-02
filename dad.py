# API project
# ask user for a joke topic
# return the number of jokes total
# randomly choose one of the jokes 
# OPTIONAL: ascii art at the beginning
import requests  # to use the get response method
from random import choice  # to choose a random joke from the results list
from termcolor import colored  # to color art
from pyfiglet import figlet_format  # to convert string below to ascii art
ascii_art = figlet_format("We love you 3000!")  # starts with fancy art
colored_ascii_art = colored(ascii_art, color="yellow")
print(colored_ascii_art)
# now to use requests module and use get method
url = "https://icanhazdadjoke.com/search"
topic = input("Let me tell you a joke! Choose a topic: ")
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()  # using .json() will allow us to use the metadata the API gives us (key, value pair)
results = response['results']  # store the giant list of dictionaries in results variable
total_jokes = response['total_jokes']
# create the outcomes of finding a joke with the user's topic
if total_jokes > 1:
    print(f"I found {total_jokes} with the topic {topic}!")
    print(f"Here is one: {choice(results)['joke']}")  # can use the choice function since results is a list
elif total_jokes == 1:
    print(f"I found one joke with the topic {topic}!")
    print(f"Here it is: {results[0]['joke']}")
else:
    print(f"Sorry, I could not find a joke with the topic {topic}. Please try again!")  # no joke could be found








