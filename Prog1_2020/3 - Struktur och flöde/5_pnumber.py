

def multiply(numbers):
    """
    multiplicera varannat nummer med 2...
    OM!!! resultat per varje siffra blir mer än 10... Korta ner....

    """
    
    #numbers = "9108220030"
    mult = ""
    i = 0
    for n in numbers:
        print(n, i)
        if i % 2 == 0:
            n = int(n)*2
        mult += shorten(n)
        i += 1
    print(mult)
    return mult

def shorten(number):
    number = int(number)
    if number >= 10:
        number -= 9
    return str(number)

def summary(numbers):
    numbers = numbers[:-1] #numbers = "910822003"
    summa = 0
    for n in numbers:
        summa += int(n)
    
    print("Summa vart:", summa)
    return summa

def find(number):
    #43
    ten = int(number/10)*10 +10
    return (ten - number)%10



pnum = input("Skriv personnummer YYMMDDXXXX:")
pnum_multiplied = multiply(pnum)
num = summary(pnum_multiplied)
control = find(num)
print("Din kontrollsiffra bör vara:", control)


