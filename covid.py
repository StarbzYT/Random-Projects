# this application scrapes the total deaths, cases and recovered
import requests  # for get request
from bs4 import BeautifulSoup  # to scrape
import re  # for regex
# use pyfiglet package and termcolor
from pyfiglet import figlet_format
from termcolor import colored
import datetime  # gets the date
import sqlite3


class App:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        age_pattern = re.compile(r"0*([0-9]{1,2})Y?")  # validates age
        match = age_pattern.search(str(age))  # only searches strings
        if match:
            self.age = age
            print(f"Greetings, {self.first}!")  # greets the user
        else:
            print(f"Sorry, {age} is not a valid age...")  # if age is not valid

    def __repr__(self):
        ascii_art = figlet_format("Welcome to the COVID-19 APP")  # starts with fancy art
        colored_ascii_art = colored(ascii_art, color="red")  # color = red
        return colored_ascii_art


class Covid:
    URL = "https://www.worldometers.info/coronavirus/#countries"

    def get_data(self):
        print("Please wait while I scrape the data...")
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, "html.parser")
        total_cases = soup.find(class_="maincounter-number").find("span").get_text().strip()  # get rid of extra space at the end of the string
        total_deaths_tag = soup.find(id="maincounter-wrap").find_next_sibling(id="maincounter-wrap")  # tag for deaths
        total_deaths = total_deaths_tag.find("span").get_text()  # actual deaths value
        total_recovered_tag = total_deaths_tag.find_next_sibling(id="maincounter-wrap")
        total_recovered = total_recovered_tag.find("span").get_text()
        date = datetime.datetime.now()  # get date when this method is run
        full_date = date.strftime("%x")  # proper format
        data = (full_date, total_cases+" cases", total_deaths+" deaths", total_recovered+" recovered")
        print("Done! \U0001f600")
        return data

    def insert_data(self, data):
        password = input("What's the password?\n")
        if password == "password":
            connection = sqlite3.connect("covid_data_db.db")  # connect to database
            cursor = connection.cursor()  # create cursor object
            query = "INSERT INTO covid VALUES (?,?,?,?)"
            cursor.executemany(query, [data])  # execute query with data
            # commit changes and close connection to database
            connection.commit()
            connection.close()
            print("The data has been transferred to the database!")
        else:
            print("That is not the password! GOODBYE!")


app = App("Starbz", "09", 16)
print(app)
covid_app = Covid()
data = covid_app.get_data()
covid_app.insert_data(data)  # give list of data to insert into database


















