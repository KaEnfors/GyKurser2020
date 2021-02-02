import cards
import time

#Boolen values
startGame = False
cardTrueOrFalse = True
cardTrueFalseBot = True
#The type of card picked
cardPicked = []
cardPickedBot = []

# Game data
allowedInput = ["C", "D", "H", "S"]
playerData = []
botData = []
i = 0
pointsBot = 0
pointsPlayer = 0

#Rounds nad lives
rounds = 10
lives = 5


# How many cards the players have
playerCard = 0
playerBot = 0
#  cards.draw_card(DECK))

lines = [[] for i in range(9)]

# Picking card start menu; for player(Input)
def startPlay():
    global cardPick, DECK
    cardPick = str(input("Please pick\n\nI want...\nC: Clubs \nD: Diamonds \nH: Hearts \nS: Spades\n "))
    if cardPick in "cheatWon":
        win()
    if cardPick in allowedInput:
        DECK = cards.build_deck(suits=[cardPick])
        shuffleCard()
        player()
    else:
        print("*****************************")
        print("Sorry, wrong input try again!")
        print("*****************************")
        startPlay()

def MainGameMenu():
    global DECK, cardPick
    input("Type K to continue\n")
    DECK = cards.build_deck(suits=[cardPick])
    shuffleCard()
    player()


#Shuffles Card
def shuffleCard():
    cards.shuffle(DECK)

#Player Data
def player():
    global rounds, rank, suit, cardTrueOrFalse, pointsPlayer
    playerCard = cards.draw_card(DECK)
    rank = playerCard["RANK"]
    suit = playerCard["SUIT"]
    asciiCard()
    rounds -= 1

    # Game storage for cards
    # if same card over 3 times then its a win
    if cardTrueOrFalse == True:
        cardPicked.append(playerCard["RANK"])
        cardTrueOrFalse = False
    if rank in cardPicked:
        playerData.append(playerCard["RANK"])
        pointsPlayer += 1
        if len(playerData) >= 5:
            win()
    print(100*"\n"+"\n****************************")
    print("*", "Player Cards:", str(pointsPlayer) + "/" + "5", "|", "Card: "+ cardPicked[0])
    print("****************************")
    # Call the bot
    playerBot()


# Enemy Data
def playerBot():
    global cardTrueFalseBot, rankbot, rounds, pointsBot
    playerBot = cards.draw_card(DECK)
    rankbot = playerBot["RANK"]
    # Game storage for cards
    # if same card over 3 times then its a win

    if cardTrueFalseBot == True:
        cardPickedBot.append(playerBot["RANK"])
        cardTrueFalseBot = False
    if rankbot in cardPickedBot:
        botData.append(playerBot["RANK"])
        pointsBot += 1
        if len(botData) >= 5:
            lose()
    print("****************************")
    print("*", "Bot Cards:", str(pointsBot) + "/" + "5", "|", "Card: "+"**")
    print("****************************")

# Card Drawer
def asciiCard():
    global suit
    if suit == "H":
        suit = "♥"
    if suit == "S":
        suit = "♠"
    if suit == "D":
        suit = '♦'
    if suit == "C":
        suit = "♣"

    lines[0].append('┌─────────┐')
    lines[1].append('│'+ suit + rank +'       │') # use two {} one for char, one for space or char.format(rank, rank))
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│    '+suit+'    │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       '+ suit + rank +'│')
    lines[8].append('└─────────┘')

# Win function
def win():
    print(100*"\n")
    def wontext2():
        print("/$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$  /$$$$$$  /$$   /$$")
        print("|  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$ /$$__  $$| $$$ | $$")
        print(" \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$| $$  \ $$| $$$$| $$")
        print("  \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$| $$  | $$| $$ $$ $$")
        print("   \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$| $$  | $$| $$  $$$$")
        print("    | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$\  $$$")
        print("    | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$ \  $$")
        print("    |__/    \______/  \______/       |__/     \__/ \______/ |__/  \__/")
    wontext2()
    quit()
#Lose function
def lose():
    print(100*"\n")
    print("!LOSER!")
    quit()



# Restart the game
# Clears the card from last round
while True:
    if startGame == False:
        startPlay()
        startGame = True
    else:
        MainGameMenu()
    for x in range(9):
        print(lines[x])
        i += 1
        if i >= 9:
            del lines[:]
            lines = [[] for i in range(9)]
            i = 0
    if lives < 1:
        quit()
        print("!YOU LOSE!")

