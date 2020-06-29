from bs4 import BeautifulSoup
import requests
import smtplib
# use pyfiglet package and termcolor
from pyfiglet import figlet_format
from termcolor import colored
# a discount program that emails you if the price on "Cracking the Coding Interview" has dropped


class Discount:

    def _get_price(self):
        URL = "https://www.chapters.indigo.ca/en-ca/books/cracking-the-coding-interview-189/9780984782857-item.html?ikwid=crack+the+coding+interview&ikwsec=Home&ikwidx=0#algoliaQueryId=108a22a9ca813caf7c1c4f2e09312a09"
        response = requests.get(URL)  # issue a get request on the url for the book
        soup = BeautifulSoup(response.text, "html.parser")
        price = soup.find(class_="item-price__price-amount")  # finds the class that contains the price
        return price.get_text()  # gets the price value of book

    def send_email(self):
        ascii_art = figlet_format("DISCOUNT APP")  # starts with fancy art
        colored_ascii_art = colored(ascii_art, color="blue")  # color = blue
        print(colored_ascii_art)
        get_price = self._get_price()
        real_price = get_price.replace("$", "")  # get rid of $ to compare with another float later
        # use SMTP method to connect
        smpt_object = smtplib.SMTP('smtp.gmail.com', 587)  # use port number
        # greet server and establish connection
        smpt_object.ehlo()  # only the recipent can recieve the message using this, no one can hack!
        # port no. 587 encrypts messages so use starttls method to initiate encryption
        smpt_object.starttls()
        # ask for email and password code
        email = input("Email: ")  # ask for the email
        password = input("Password: ")  # password for login
        smpt_object.login(email, password)  # use login method to login into the gmail account
        from_address = email  # from input email
        to_address = email  # to input email (can be any other email)
        if float(real_price) < 49.95:  # compare the scraped price to the original price
            subject = "Discount Found!"  # subject heading for email
            message = "Crack the Coding Interview is on sale!\nGo here: https://www.chapters.indigo.ca/en-ca/books/cracking-the-coding-interview-189/9780984782857-item.html?ikwid=crack+the+coding+interview&ikwsec=Home&ikwidx=0#algoliaQueryId=108a22a9ca813caf7c1c4f2e09312a09"
            msg = "Subject: "+subject+"\n"+message  # use this syntax to form the massage

            smpt_object.sendmail(from_address, to_address, msg)  # sends the msg from the adress and to the adress given (plus msg)
            print("Check your email! I found a discount!")  # tell the user to check their email if discount is found
            smpt_object.quit()  # close connection when done, similiar to http requests and sqlite3
        else:
            print("Sorry, I could not find a discount...")  # otherwise, print this


price = Discount()
price.send_email()






