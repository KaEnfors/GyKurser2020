import time, sys

GAME = True
dinomap = [
    ("░" * 75),
    ("░" * 75),
    ("░" * 75)

]
dino = [
    "   /¨>",
    " ┌/ ┌┘",
    "_/| | "
]
obs = "█"


print("Dinogame!")
framcount = 0
while GAME:

    frame = dinomap.copy()
    frame[0] = frame[0][:7] + dino[0] + frame[0][8:]
    frame[1] = frame[1][:7] + dino[1] + frame[1][8:]
    frame[2] = frame[2][:7] + dino[2] + frame[2][8:]

    print(frame[0], frame[1], frame[2], end="\n", sep="\n")
    framcount += 1
    time.sleep(0.3)
    sys.stdout.write("\033[F") #clear
    sys.stdout.write("\033[F") #clear
    sys.stdout.write("\033[F") #clear



    

