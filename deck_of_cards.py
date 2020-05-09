from random import shuffle  # used to shuffle the deck
# read instructions on Deck of Cards section, #249


class Card:
    def __init__(self, value, suit):
        self.value = value  # attribute for value of card
        self.suit = suit  # attribute for suit of card

    def __repr__(self):  # runs automatically to present deck
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):  # create unshuffled deck
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))  # add each possibility of cards to self.cards list

    def __repr__(self):  # presents deck object
        return "Deck of {} cards".format(self.count())

    def count(self):  # use this method to check the length of the list at any time
        return len(self.cards)

    def _deal(self, num):  # internal method, not to be called outside
        count = self.count()
        actual = min([count, num])
        if count == 0:  # if there are no more cards left to be dealt
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]  # takes actual number of cards from the deck
        self.cards = self.cards[:-actual]  # updates deck to disinclude the cards taken away
        return cards

    def deal_card(self):  # gives only one card
        return self._deal(1)[0]  # we do not want a list back so only gives first index of list

    def deal_hand(self, hand_size):  # takes a specific value for how many cards
        return self._deal(hand_size)  # this time we want a list since there is more than one card

    def shuffle(self):
        if self.count() < 52:  # prevents the deck to be shuffled after it has been used
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self









