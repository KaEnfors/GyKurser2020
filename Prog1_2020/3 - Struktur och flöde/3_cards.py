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

player = 0
scores = [0,0,0,0]
score = 0

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
    print("playing game....")
    game = input("continue? y/n:").startswith('y')
