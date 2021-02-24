#Higher or Lower v1.0
#Skapad med kärlek av Noah och Adonay 

import random

score = 0
game = True

rulesli = ['Help', 'help', 'HELP']
high = ['H', 'h', 'HIGHER', 'Higher', 'higher']
low = ['L', 'l', 'LOWER', 'Lower', 'lower']
yes = ['Y', 'y', 'YES', 'Yes', 'yes']
no = ['N', 'n', 'NO', 'No', 'no']

suits = ['H', 'S', 'D', 'C']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

suit1 = (random.choice(suits))
suit2 = (random.choice(suits))
rank1 = (random.choice(ranks))
rank2 = (random.choice(ranks))

print('------')
print('Welcome to')
print('H I G H E R  O R  L O W E R')
print()
print('Made by Nowalzky & Adon')
print()
print('Write "Help" to read about how the game works,')
print('or press ENTER to start the game.')
print('------')

rules = input('> ')
print('------')

if rules in rulesli:

    print('Higher or Lower is a really easy game to play.')
    print("You, the player, must guess whether the next card's value will be higher or lower than the previous card's value.")
    print('In this verison of the game Ace is high.')
    print()
    input('Press ENTER when you are ready to play...')
    print('------')

print('Card:', suit1 + rank1)
print()

while game:
    askforreplay = True
    card1 = suit1 + rank1
    card2 = suit2 + rank2

    print('Next card; Higher or Lower than ',rank1,'?',sep='')
    choice = input('H/L: ')
    print('------')

    if choice in high and ranks.index(rank2) > ranks.index(rank1) or choice in low and ranks.index(rank2) < ranks.index(rank1):
        print('Old card:',card1)
        print('New card:',card2)
        print()
        print('Correct! Score incresed by one!')
        print('Moving on...')
        print('------')
        score = score +1
        print('Current score:',score)
        print('Current card:',card2)
        print()
        suit1 = suit2
        rank1 = rank2
        suit2 = (random.choice(suits))
        rank2 = (random.choice(ranks))

    elif choice in high and ranks.index(rank2) == ranks.index(rank1) or choice in low and ranks.index(rank2) == ranks.index(rank1):
        print('Old card:',card1)
        print('New card:',card2)
        print()
        print('Tie! Score unchanged!')
        print('Moving on...')
        print('------')
        print('Current score:',score)
        print('Current card:',card2)
        print()
        suit1 = suit2
        rank1 = rank2
        suit2 = (random.choice(suits))
        rank2 = (random.choice(ranks))

    elif choice in high and ranks.index(rank2) < ranks.index(rank1) or choice in low and ranks.index(rank2) > ranks.index(rank1):
        print('Old card:',card1)
        print('New card:',card2)
        print()
        print('Wrong, you lose!')
        print('------')
        print('Final score:',score)
        print()
        score = 0

        while askforreplay:
            print('Wanna play again?')
            again = input('Y/N: ')
            print('------')
        
            if again in no:
                print('Thanks for playing!')
                print('------')
                askforreplay = False
                game = False

            elif again in yes:
                print('Staring over...')
                print('Score set to 0')
                print('------')
                rank1 = (random.choice(ranks))
                suit1 = (random.choice(suits))
                rank2 = (random.choice(ranks))
                suit2 = (random.choice(suits))
                print('Card:',suit1 + rank1)
                print()
                askforreplay = False

            else:
                print('Error, use Y or N!')
                print()

    else:
        print('Error, use H or L!')
        print()
        print('Current card:',card1)