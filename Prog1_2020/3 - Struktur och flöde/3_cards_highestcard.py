"""

- listor
- beräkningar
- jämförelser
- loopar
- funktioner


"""

# Vad ska finnas?
    # - kort
    # - kortlek
    # - spelare
    # - poäng
    # - spelrunda/omgång/parti
    # - ? 
    #  
# Hur ska det fungera??
    # - kort kan vara två bokstäver, ex: HQ
        # kort = "S8". färgen = kort[0] = 'S', ranken = kort[1] = '8'
    # - kortlek är en lista... färger är en lista, ranker är en lista
    # spelare kan vara en siffra?
    # poäng kan vara en lista, eller bara en spelare
import random


players = [0, 0]

game = True

deck = []
suits = ['H', 'S', 'D', 'C']
ranks = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A',
]

for suit in suits:
    for rank in ranks:
#        print("card:", suit + rank)
        deck.append(suit + rank)
print(deck)


while game:
#    card = deck[-1]
#    deck.remove(card)

    player1card = random.choice(deck)
    deck.remove(player1card)
    player2card = random.choice(deck)
    deck.remove(player2card)

    print("Player 1 draws:", player1card)
    print("Player 2 draws:", player2card)

    #Jämför båda korten
    #genom att... Kolla om spelare 1 vann...

    print(player1card[1:], "vs", player2card[1:])
    rank1 = ranks.index(player1card[1:])
    rank2 = ranks.index(player2card[1:])
    print(rank1, "vs", rank2)

    """
    rank1 = player1card[1:]
    if rank1 == 'J':
        rank1 = 11
    elif rank1 == 'Q':
        rank1 = 12
    elif rank1 == 'K':
        rank1 = 13
    elif rank1 == 'A':
        rank1 = 14
    else:
        rank1 = int(rank1)

    rank2 = player2card[1:]
    if rank2 == 'J':
        rank2 = 11
    elif rank2 == 'Q':
        rank2 = 12
    elif rank2 == 'K':
        rank2 = 13
    elif rank2 == 'A':
        rank2 = 14
    else:
        rank2 = int(rank2)

    """
#    print(rank1, "vs", rank2)

    if rank1 > rank2:
        players[0] += 1
        print("Player1 gets points!")
    elif rank2 > rank1:
        players[1] += 1
        print("Player2 gets points!")
    else:
        print("Draw!")
    
    print("Player1 has", players[0], "points!")
    print("Player2 has", players[1], "points!")
    # Ge poäng till spelaren med höst kort.
    


    game = input("continue? y/n:").startswith('y')
    if len(deck) <2:
        print("Game over!")
        exit()

