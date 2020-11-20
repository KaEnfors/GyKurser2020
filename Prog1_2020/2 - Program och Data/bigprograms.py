


def input_int(msg : str):
    entry = input(msg)
    while not entry.isdigit():
        entry = input("Only number allowed: ")

    return int(entry)


def get_next_ten(summa : int):
    if(summa % 10 == 0):
        return summa

    summa //= 10 #5
    summa += 1  #6
    summa *= 10 # 60

    return summa

num = input_int("Enter integer:")
num2 = input_int("Enter another integer")
ctrl = get_next_ten(num) - num
print(ctrl)
