import sqlite3
import requests
from bs4 import BeautifulSoup

# scrape all books

URL = "http://books.toscrape.com/"


def scrape_books():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all(class_="product_pod")  # articles have class that has access to all the book data
    all_books = []  # list of tuple infrmation for all books
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))  # store all data in one variable which is a tuple
        all_books.append(book_data)
    save_books(all_books)  # after loop, save the books to the books database

# insert book data into a database


def save_books(all_books):
    connection = sqlite3.connect("books_db.db")
    cursor = connection.cursor()
    query = "INSERT INTO new_books VALUES (?,?,?)"
    cursor.executemany(query, all_books)
    # commit changes and close connection to database
    connection.commit()
    connection.close()


# get titles


def get_title(book):
    title = book.find("h3").find("a")["title"]
    return title

# get the prices


def get_price(book):
    price = book.find(class_="price_color").get_text()
    cad_price = round(float(price[2:]) * 1.52, 2)
    return '$' + str(cad_price)

# get ratings


def get_rating(book):
    ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 3}
    paragraph = book.find(class_="star-rating")  # gives a list of one element
    text = paragraph.get_attribute_list("class")[-1]  # gets the star rating
    if ratings[text] == 1:
        return f"1 star"  # text gives word of number and ratings returns the actual number
    return f"{ratings[text]} stars"


scrape_books()








