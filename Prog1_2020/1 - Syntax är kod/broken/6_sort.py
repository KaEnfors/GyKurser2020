"""
Sorteringsalgoritm

"""
import random

NUMBERS = []

num = 0
while num < 50:
    NUMBERS.append(num)
    num = num + 1

random.shuffle(NUMBERS)

print("Shuffled:", NUMBERS)
i,j = 0,0
while i < len(NUMBERS) -1:
    j = 0
    while j < len(NUMBERS) -1:
        if(NUMBERS[j] > NUMBERS[j+1]):
            tmp = NUMBERS[j+1]
            NUMBERS[j+1] = NUMBERS[j]
            NUMBERS[j] = tmp
        j = j+1
    i = i+1

print("Sorted:", NUMBERS)