"""
Bubbelsorteringsalgoritm

"""
import random

def bubblesort(LIST):
    n = len(LIST)
    for num in LIST:
        for i in range(n-1):
            if LIST[i]>LIST[i+1]:
                tmp = LIST[i]
                LIST[i] = LIST[i+1]
                LIST[i+1] = tmp
    return LIST

NUMBERS = [num for num in range(0, 20, 1)]
random.shuffle(NUMBERS)
print("NOT SORTED\t",NUMBERS)
NUMBERS = bubblesort(NUMBERS)
print("SORTED\t\t",NUMBERS)



