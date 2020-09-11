"""



"""
import random

def print_card(card:dict):
    """
    Print a card from dictionary
    """

    if card['SUIT'] == "H":
        print("♥", card['RANK'])
    if card['SUIT'] == "S":
        print("♠", card['RANK'])
    if card['SUIT'] == "D":
        print("♦", card['RANK'])
    if card['SUIT'] == "C":
        print("♣", card['RANK'])


def build_deck(withJokers=False):
    """
    Builds a deck, and returns sorted deck
    """
    DECK = []
    for suit in suits():
        for rank in ranks():
            new_card = {
                "RANK": rank,
                "SUIT": suit
            }
            DECK.append(new_card)

    return DECK

def draw_card(cards:list, randomly=False):
    """
    Draw a card from list.
    @param randomly, False (default) for top card, True for random
    """

    if randomly:
        card = cards.pop(random.randint(0, len(cards)))
        return card

    return cards.pop(0)

def give_card(cards, card):
    """
    Adds a card to a list of cards
    """
    cards.append(card)

def shuffle(cards:list):
    """
    Shuffle a list of cards in random order
    @return shuffled list of cards
    """
    random.shuffle(cards)

def ranks():
    return [
        "2", "3", "4", "5",
        "6", "7", "8", "9",
        "10", "J", "D", "K", "A",
    ]

def suits():
    return [
        "H",
        "S",
        "D",
        "C"
    ]


