"""



"""

def print_card(card:dict):
    """
    Print a card from dictionary
    """
    pass

def draw_card(cards:list, randomly=False):
    """
    Draw a card from list.
    @param randomly, False (default) for top card, True for random
    """
    return ""

def give_card(cards, card):
    """
    Adds a card to a list of cards
    """
    pass

def shuffle(cards:list):
    """
    Shuffle a list of cards in random order
    @return shuffled list of cards
    """
    return ""


CARD_RANKS = [
    "2", "3", "4", "5",
    "6", "7", "8", "9",
    "10", "J", "D", "K", "A",
]

CARD_SUITS = [
    "H",
    "S",
    "D",
    "C"
]

DECK = []

for suit in CARD_SUITS:
    for rank in CARD_RANKS:
        new_card = {
            "RANK": rank,
            "SUIT": suit
        }
        DECK.append(new_card)


for card in DECK:
    print(card['SUIT'] + card['RANK'] + "\t",card)
