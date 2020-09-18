import cards


DECK = cards.build_deck()
cards.shuffle(DECK)

PLAYER1 = cards.draw_card(DECK)
PLAYER2 = cards.draw_card(DECK)

print(PLAYER1['RANK'])
print(PLAYER2['RANK'])

for rank in cards.ranks():
    if PLAYER1['RANK'] == PLAYER2['RANK']:
        print("Tie!")
        break

    if rank == PLAYER1['RANK']:
        print("Player 2 wins...")
        break
    if rank == PLAYER2['RANK']:
        print("Player 1 wins...")
        break

"""
points = {
    'A' : 14,
    'K' : 13,
    'D' : 12,
    'J' : 11,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

if (points[PLAYER1['RANK']] > points[PLAYER2['RANK']]):
    print("Player 1 won...")
else:
    print("Player 2 won...")
"""