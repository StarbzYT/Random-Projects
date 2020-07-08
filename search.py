# search google maps
from twilio.rest import Client  # # send msgs with python
import auth  # custom module for authentication data


class Search:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_location(self):
        search = input(f"Hi {self.first}, where would you like to go?\n").strip() # strip all spaces to attach to URL
        if search:
            account_sid = auth.account_sid()  # verify their account_sid to prevent spam
            auth_token = auth.auth_token()  # verify it is them

            client = Client(account_sid, auth_token)  # set up client to authenticate

            phone_number = input("What is your phone number?\n")  # recipient (can be changed to a fixed number)
            from_ = auth.trial()  # sender

            message = client.messages.create(  # create the msg and send!
                to=phone_number,  # input
                from_=from_,  # from auth module
                body=f"Here are some locations for {search} https://www.google.com/maps/search/{search.replace(' ', '')}")  # link with location

            print(message)
            print(f"I sent you some location(s) for {search}!")
        else:
            print("You did not enter a location...")  # if input is falsy


location = Search("Starbz", "09")
location.get_location()










