""" Game of War """

from random import shuffle

# Suit, Rank, Value
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        # Value to corrolate with the inputed rank
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
        'Six': 6, 'Seven': 7, 'Eight': 8,
        'Nine': 9, 'Ten': 10, 'Jack': 11,
        'Queen': 12, 'King': 13, 'Ace': 14}

class Card:
    """ Card class, gives information about each individual card """
    def __init__(self, suit, rank): #no need to input value
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        """ Prints the description of the card given """
        return self.rank + " of " + self.suit

class Deck:
    """ Creates a new deck for each player """
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            # For every possible card combination,
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # For War
            self.all_cards.extend(new_cards)
        else:
            # For a single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# GAME SETUP
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Game Logic
game_on = True
round_num = 0
while game_on: # While game is on
    round_num += 1
    print(f'Round {round_num}')

    at_war = True

    if len(player_one.all_cards) == 0:
        print('Player Two Wins!')
        break
    elif len(player_two.all_cards) == 0:
        print('Player One Wins!')
        break
    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # While at war
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war')
                print('Player Two wins!')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('Player One wins!')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
