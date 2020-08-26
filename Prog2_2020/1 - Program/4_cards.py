"""



"""

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
