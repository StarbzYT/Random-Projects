# this code does not need to be run every time to play the game!
# quotes guessing game
import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"  # base url that will be attached with url


def scrape_quotes():
    data = []  # append everything scraped to this list
    url = "/page/1"  # start with page 1
    while url:  # while loop will become false if there is no url (next button) and will represent whatver it found until then
        response = requests.get(f"{BASE_URL}{url}")
        print(f"Now scraping {BASE_URL}{url}...")
        soup = BeautifulSoup(response.text, "html.parser")  # response.text is HTML
        quotes = soup.find_all(class_="quote")  # find all quotes attr to loop through later

        for quote in quotes:
            quote_ = quote.find("span").get_text()  # quote is text in span tag
            author = quote.find("small").get_text()  # author is text in small tag
            bio_link = quote.find("a")["href"]  # link is an attr in a tag
            data.append({"quote": quote_, "author": author, "Bio-Link": bio_link})
            next_button = soup.find(class_="next")  # track and see if there is a next button on each page
            url = next_button.find("a")["href"] if next_button else None  # update url if next button otherwise the while stops
            sleep(2)  # be polite and slow down the while loop from scraping all pages rapidly
    return data  # retrieves data list to be used for play_game func


# write quotes to csv file
def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["quote", "author", "Bio-Link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:  # quotes is a list!
            csv_writer.writerow(quote)


quotes = scrape_quotes()  # is a list of dicts
write_quotes(quotes)





