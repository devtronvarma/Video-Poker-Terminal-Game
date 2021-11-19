# Import packages
import random
import pyfiglet
import sys  # for showing hands horizontally

# Print Welcome Message to Kick Off Game
welcome_msg = pyfiglet.figlet_format("WELCOME TO \n VIDEO POKER")
# print(welcome_msg)

# Define Card class
import random

class Card:

    card_values = {  # value of the ace is high until it needs to be low
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

# Function to output ascii version of the cards in a hand in the terminal
def ascii_version_of_card(*cards, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == 10:  # ten is the only one who's rank is 2 char long
            rank = str(card.rank)
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = str(card.rank)[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result

# Define Deck class 
class Deck:
    
    def __init__(self):
        self.cards = []
        self.build()

    # method for building the deck
    def build(self):
        for s in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for v in range(2, 11):
                self.cards.append(Card(s,v))
            for c in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(s,c))

    # method to show cards in deck
    def display(self):
        for c in self.cards:
            print(ascii_version_of_card(c))

    # method to shuffle cards in deck
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # method to draw card from the deck
    def draw_card(self):
        return self.cards.pop()

# Define Player Class
class Player:
    def __init__(self):
        self.hand = []
        self.bankroll = 20

    # method for initial two-card draw
    def draw_cards(self, deck):
        for i in range(5):
            self.hand.append(deck.draw_card())
        return self

    # method for displaying player's hand
    def show_hand(self):
        print(ascii_version_of_card(
                self.hand[0],
                self.hand[1],
                self.hand[2],
                self.hand[3],
                self.hand[4]))

    # method for placing a bet
    def bet(self):
        self.bet_size = input("How many coins would you like to bet? (Max: 5)\n") 
        print("You bet {} coins.".format(self.bet_size))

    # method for selecting cards to redraw
    def redraw(self):
        redraw_yn = input("Do you want to redraw any cards? Y/N \n").capitalize()
        if redraw_yn == "Y":
            redraw_num = int(input("How many cards do you want to redraw?\n"))
            if redraw_num > 1:
                redraw_list = [int(x) - 1 for x in input("Which cards do you want to redraw? (Use commas to separate) \n").split(',')]
                for i in redraw_list:
                    self.hand[i] = deck.draw_card()    
            else:
                redraw_index = int(input("Which card do you want to redraw? \n")) - 1
                self.hand[redraw_index] = deck.draw_card()

            # print new hand
            print("Your hand is now: \n")
            self.show_hand()        

# Define Hierarchy of Hands
# Function to determine flush
def is_flush(hand):
    return all(x.suit == hand[0].suit for x in hand)

# def is_straight(hand):
        # sorted_hand = sorted(hand)
        # for i in range(len(hand)):
        #     hand[i + 1].rank == hand[i].rank + 1 for i in hand


# Testing Functionality
# deck = Deck()
# deck.shuffle()

# player = Player()
# player.draw_cards(deck)
# player.show_hand()
# player.redraw()

# Create function to score hand
def score_hand(hand):
    points = sorted([hand[i].points for i in range(5)])
    suits = [hand[i].suit for i in range(5)]
    points_repeat = [points.count(i) for i in points]
    suits_repeat = [suits.count(i) for i in suits]
    diff = max(points) - min(points)

    # return points_repeat 

    if 5 in suits_repeat:
        if points == [10, 11, 12, 13, 14]: #find royal flush
            return "Royal Flush"
        elif diff == 4 and max(points_repeat) == 1: # find straight flush w/o ace low
            return "Straight Flush"
        elif diff == 12 and points[4] == 14: # find straight flush w/ace low
            check = 0
            for i in range(1, 4):
                check += points[i] - points[i - 1]
            if check == 3:
                return "Straight Flush"
            else:
                return "Flush"
        else:
            return "Flush"
    elif sorted(points_repeat) == [2,2,3,3,3]: # find full house
        return "Full House"
    elif 4 in points_repeat: # find four of a kind
        return "Four of a Kind"
    elif 3 in points_repeat: # find three of a kind
        return "Three of a Kind"
    elif points_repeat.count(2) == 4: # find two-pair
        return "Two Pair"
    elif diff == 4 and max(points_repeat) == 1: # find straight w/o ace low
            return "Straight"
    elif diff == 12 and points[4] == 14: # find straight w/ace low
        check = 0
        for i in range(1, 4):
            check += points[i] - points[i - 1]
        if check == 3:
            return "Straight"

print(score_hand(hand))

