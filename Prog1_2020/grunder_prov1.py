
x = 31
y = 15
c = x % y 

print("1", x+y) 
print("2", c + y % c)
print("3", x % c + y)



x = "Joe"
y = "Biden"

print("4", y*2)
print("5", 'Y'*5 + x,y + y[-1]*5)

print("6", (x*5).count('o'))
print("7", (x + " " + y).count('r') )




x = "I will write potato in the chat"
y = x[0]
y += x[-1]
y += x[5]
z = x.index('w')
y += (x[3])
print("8", y.lower())



def woop(n, inc):
    return n + inc

i = 0

while i > -20:
    i = woop(i, -1)
    
print("9", i)



x = 'a'
if(x in "APA"):
    print("10", "gurka!")
else:
    print("10", "ingen gurka!")


x = "Python is awesome".count('o')
if x > 10 or x <3:
    x *= "or is it?".count('i')
    if x > 0 and x < 20:
        print("11", "Yep!")
    else:
        print("11", "Nope!")
else:
    print("11", "Def. nope!!")


x = 4
y = ""
while x%9 != 0:
    x += 8
    y +=  str(x) + ","
print("12", y)


x = 0
for a in range(0,5,2):
    for b in range(0,8,3):
        x += b
print("13", x)


def con(z):
    return z**2
i = 2
while not con(i) > 20:
    i = con(i)

print("14:", i)

