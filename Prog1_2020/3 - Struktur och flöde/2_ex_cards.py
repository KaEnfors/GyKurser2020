"""



"""

import time, os, random

def userchoice():
    while True:
        choice = input("higher or lower?")
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
            else:
                print("Faulty input...")
        else:
            print("Faulty input...")
    return choice

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1

random.shuffle(deck)
score = 0
card1 = deck.pop(0)

while True:
    os.system("cls") # linux "clear
    print("Your score so far is", score)
    print("\n\nThe current card is", card1[0])
    choice = userchoice()
    choice2 = userchoice()

    card2 = deck.pop(0)
    print("The next card picked is", card2[0])
    time.sleep(1)

    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Correct!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print("Wrong!")
        time.sleep(1)
        break
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Correct!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("Wrong!")
        time.sleep(1)
        break
    else:
        print("draw!")

    card1 = card2

os.system("cls")
print("Game over!")
print("You final score is", score)
time.sleep(4)
os.system("cls")