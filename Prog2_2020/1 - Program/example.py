import random

HANGMAN_WORDS = [
    'python',
    'machine learning',
    'developer',
    'coffee',
    'deadline',
    'error',
    'compiler',
]

LETTERS = []

CORRECT = random.choice(HANGMAN_WORDS)
CURRENT = "_" * len(CORRECT)
LIVES = 10

def win():
    global CORRECT
    print()
    print("You win! :)")
    print("The word was:", CORRECT.capitalize())
    print()
    exit()

def lose():
    global CORRECT
    print()
    prit("You lose! :(")
    print("The word was:", CORRECT.capitalize())
    print()
    exit()

def hit():
    global LIVES
    LIVES -= 1
    hanged_man()
    


def hang_input():
    global LETTERS
    global CORRECT(
    print("Guess letter or word.")
    inp = input("enter: ")
    if(len(inp) > 1):
        if(inp.lower() == CORRECT):
            win()
            return ''
        else:
            hit()
            return ''
    inp = inp.lower()[0]
    if(inp in LETTERS or inp.isdigit()):
        print("Enter valid letter")
        return hang_input()
    return inp

def hanged_man():
    global LIVES
    print("___________..________")
    print("| .__________))______|")
    if(LIVES >8): return
    print("| | / /      || ")
    print("| |/ /       ||")
    if(LIVES >7): return
    print("| | /        ||.-''.")
    print("| |/         |/  _  \ ")
    print("| |          ||  `/,|")
    if(LIVES >6): return
    print("| |          (\\\\`_.'")
    print("| |         .-`--'.")
    if(LIVES >5): return
    print("| |        /Y . . Y\ ")
    print("| |       // |   | \\\\")
    if(LIVES >4): return
    print("| |      //  | . |  \\\\")
    print("| |     ')   |   |   (`")
    if(LIVES >3): return
    print("| |          ||'||")
    print("| |          || ||")
    print("| |          || ||")
    if(LIVES >2): return
    print("| |          || ||")
    print("|  \        / | | \ ")
    print("|   \       `-' `-'    ")
    if(LIVES >1): return
    print("| |\ \                ")
    print("| | \ \               ")

def play():
    global LETTERS, LIVES, CORRECT, CURRENT
    guess = hang_input()
    if(guess in CURRENT):
        print("Already guessed that...")
    elif(guess in CORRECT):
        for i in range(len(CORRECT)):
            if(CORRECT[i] == guess):
                CURRENT = CURRENT[:i] + guess + CURRENT[i+1:]
        print('Correct!')
    elif(guess == ''):
        pass
    else:
        LETTERS.append(guess)
        hit()

    print(LETTERS)
    print(CURRENT)   


while LIVES > 0:
    play()
else:
    lose()
