#Imports a module
import os
import random
# esteregg
muskOnline = False

#It's set of words (list)
HANGMAN_WORDS = [
   'python',
   'machine learning',
   'developer',
   'coffee',
   'deadline',
   'error',
   'compiler',
]

textStar = """            .                                            .\n     *   .                  .              .        .   *          .\n  .         .                     .       .           .      .        .\n        o                             .                   .\n         .              .                  .           .
          0     .\n                 .          .                 ,                ,    ,\n .          \          .                         .
      .      \   ,\n   .          o     .                 .                   .            .\n     .         \                 ,             .                .\n               #\##\#      .                              .        .
\n             #  #O##\###                .                        .\n   .        #*#  #\##\###                       .                     ,        .   ##*#  #\##\##               .                     .\n      .      ##*#  #o##\#         .                             ,       .\n          .     *#  #\#     .                    .             .          ,\n                      \          .                         .\n____^/\___^--____/\____O______________/\/\---/\___________---______________\n   /\^   ^  ^    ^                  ^^ ^  \ ^          ^       ---
         --           -            --  -      -         ---  __       ^\n   --  __                      ___--  ^  ^                         --  __"""

#Letters that have been tried
LETTERS = []
#Picks a random word from ANGMAN_WORDS list
# Len() is a function which returns the number of items (length) in an object.
# Replaces alphabets with _
CORRECT = random.choice(HANGMAN_WORDS)
CURRENT = "_" * len(CORRECT)
# The users tries
LIVES = 10

# Function is a block of code, which only runs when it called. E.g win()
# Global makes the variable public so it can be used by everyone, both inside of function and outside
# This is called when the user wins.
# capitalize() makes the word capitalized.
def win():
   global CORRECT
   print()
   print("You win! :)")
   print("The word was:", CORRECT.capitalize())
   print()
   exit()

# This function is called when the user loses.
def lose():
   global CORRECT
   print()
   print("You lose! :(")
   print("The word was:", CORRECT.capitalize())
   print()
   exit()

# This function is called when the user guesses wrong.
# Calls the function hanged_man() which prints the figure.
# Adds -1 to the lives
def hit():
   global LIVES
   LIVES -= 1
   hanged_man()

# inp is a variable which takes input from user(Letters)
# if statement checks whatever if inp is greater then 1, if it is greater it will then checks if inp is in the CORRECT list.
# if the user guessed it right, it will call win()
# Or if the user guessed it wrong, it will call hit()
def hang_input():
   global LETTERS
   global CORRECT
   global inp
   print("Guess letter or word.")
   inp = input("enter: ")
   elon()
   if (len(inp) > 1):
       if (inp.lower() == CORRECT):
           win()
           return ''
       else:
           hit()
           return ''
   # lower()[0] takes the first latter
   # If the input the user gave is unveiled like digits(And letter), then it will return back; It will recall it self.
   inp = inp.lower()[0]
   if (inp in LETTERS or inp.isdigit()):
       print("Enter valid letter")
       print("poop")
       return hang_input()
   # Returns the user input
   return inp

# Checks if the variable is bigger then x then it will print the figure in order according to the lives left.
def hanged_man():
   global LIVES
   print("___________..________")
   print("| .__________))______|")
   if (LIVES > 8): return
   print("| | / /      || ")
   print("| |/ /       ||")
   if (LIVES > 7): return
   print("| | /        ||.-''.")
   print("| |/         |/  _  \ ")
   print("| |          ||  `/,|")
   if (LIVES > 6): return
   print("| |          (\\\\`_.'")
   print("| |         .-`--'.")
   if (LIVES > 5): return
   print("| |        /Y . . Y\ ")
   print("| |       // |   | \\\\")
   if (LIVES > 4): return
   print("| |      //  | . |  \\\\")
   print("| |     ')   |   |   (`")
   if (LIVES > 3): return
   print("| |          ||'||")
   print("| |          || ||")
   print("| |          || ||")
   if (LIVES > 2): return
   print("| |          || ||")
   print("|  \        / | | \ ")
   print("|   \       `-' `-'    ")
   if (LIVES > 1): return
   print("| |\ \                ")
   print("| | \ \               ")
# This function starts the game
# Makes the function call to a variable
#Checks if guess is in CURRENT if it is.
# Checks if the guess is correct, adds the letter to the "_" line
def play():
   global LETTERS, LIVES, CORRECT, CURRENT
   guess = hang_input()
   if (guess in CURRENT):
       print("Already guessed that...")
   elif (guess in CORRECT):
       for i in range(len(CORRECT)):
           if (CORRECT[i] == guess):
               CURRENT = CURRENT[:i] + guess + CURRENT[i + 1:]
   # If guess is not given it will pass
       print('Correct!')
   elif (guess == ''):
       pass
   #When wrong it will append and call hit()
   else:
       LETTERS.append(guess)
       hit()

   print(LETTERS)
   print(CURRENT)
# The hidden content.

def elon():
   global inp
   global muskOnline
   print(inp + "Is there?")
   if (inp.lower() == "elonmusk"):
         print("Elon is Online!")
         print("\n" * 100)
         muskOnline = True

   # While lives is bigger then 0, the code will loop until it reach 0
while LIVES > 0:

   if(muskOnline == True):
      print("\n" * 100)
      print(textStar)
      input("")
   elif(muskOnline == False):
      play()
else:
   lose()