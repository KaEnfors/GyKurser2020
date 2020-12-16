import time, sys

GAME = True

map = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]


print("Tic-tac-toe!")
while GAME:
    
    print(map[0][0],map[0][1],map[0][2], sep="|", end="\n")
    print(map[1][0],map[1][1],map[1][2], sep="|", end="\n")
    print(map[2][0],map[2][1],map[2][2], sep="|", end="\n")


    input("Enter number:")
    sys.stdout.write("\033[F") #clear 
    sys.stdout.write("\033[F") #clear 
    sys.stdout.write("\033[F") #clear
    sys.stdout.write("\033[F") #clear
#    sys.stdout.write("\033[F") #clear
#    sys.stdout.write("\033[F") #clear



    

