
print("Hello world")

varname = "Hello world from variable"
print(varname)

input("press enter...")
print("\n\n\n\n\n\n\n")

value = 75
othervalue = 20.2

print("Type of text:", type(varname))
print("Type of number:", type(value))
print("Type of decimal:", type(othervalue))

input("press enter...")
print("\n\n\n\n\n\n\n")

valuefrominput = input("Enter some text:")
print("You entered:", valuefrominput, "which is", type(valuefrominput))
valuefrominput = input("Enter a NUMBER:")
print("You entered:", valuefrominput, "which is", type(valuefrominput))
integerfrominput = int(valuefrominput)
print("Convert text-numbers to real integer with int(value)", integerfrominput)

input("press enter...")
print("\n\n\n\n\n\n\n")

num1 = 12
num2 = 15
print("* + - / can be used to calculate")
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
print(num2, "%", num1, "=", num2 % num1)
input("press enter...")
print("\n\n\n\n\n\n\n")

# Listor och dictionary
    # Strängar är listor

mylistofstuff = [123,421,7654,2675,3234,7432,92342]
otherlist = [9,7, 1 ,4, 6, 4, 5]
mergedlist = mylistofstuff + otherlist

print("Some lists...")
print(mylistofstuff)
print(otherlist)
print(mergedlist)
print("Access values in list with brackets list[NUMBER]", otherlist[2])

mydictofstuff = {
    "thing1" : 25,
    "otherthing" : 77,
    "somename" : "somevalue"
}
print("Some dict...")
print(mydictofstuff)
print("Access values in dict with brackets dict[NAME]", mydictofstuff['otherthing'])


input("press enter...")
print("\n\n\n\n\n\n\n")

print("77 > 55 =", 77 > 55)
print("77 == 55 =", 77 == 55)
print("77 < 55 =", 77 < 55)
print("77 != 55 =", 77 != 55)
print("55 < 55 =", 55 < 55)


input("press enter...")
print("\n\n\n\n\n\n\n")

print("Vilkorlig kod")

if(55 < 100):
    print("1. 55 < 100 =",55 < 100, "So this code vill run")
    
if(77 < 55):
    print("2. 55 < 100 =",77 < 55, "So this code vill not run")

if(77 < 55):
    print("3. 55 < 100 =",77 < 55, "So this code vill run")
else:
    print("3. 55 < 100 =",77 < 55, "So this code vill run from the else statement")

input("press enter...")
print("\n\n\n\n\n\n\n")

num = 0
while(num < 10):
    print("Num is now:", num)
    num += 1

while(num >= 0):
    print("Num is now:", num)
    num -= 2


input("press enter...")
print("\n\n\n\n\n\n\n")

listofnumbers = [11,21,5,13,96,86,94,73,5,12,5,7,8,89,5,4,56,7]
# for in list och range

lengthoflist = len(listofnumbers)
i = 0
while (i < lengthoflist):
    print("Item on position", i, "is", listofnumbers[i])
    i += 1

print("Quickly step through lists with for-in-statement")
for number in listofnumbers:
    print("Thing in list:", number)

input("press enter...")
print("\n\n\n\n\n\n\n")

print("Quickly iterate over numbers with range, but you dont know the position then")
for x in range(10):
    print("x is now:", x)

input("press enter...")
print("\n\n\n")

for y in range(0,20,2):
    print("y is now:", y)

input("press enter...")
print("\n\n\n")

for z in range(0,1000,7):
    print("z is now:", z)

print("Type of range is:", type( range(10) ) )

