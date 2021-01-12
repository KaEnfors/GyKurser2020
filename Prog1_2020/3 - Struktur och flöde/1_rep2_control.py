"""
Jämförelser och if/while

"""


x = 7

print(x > 5)
print(x < 5)
print(x == 7)
print(x == 8)
print(x != 7)
print(x != 8)
print(x > 7)
print(x < 7)
print(x >= 7)
print(x <= 7)



print("Del 2")‌‌ 
y = "Programmering"
print(len(y) > 10)
print(y.endswith('g'))
print(y.startswith('P'))‌‌ 
print(y.startswith('p'))
print("ring" in y)
print(not y.startswith('p'))
print(not y.startswith('P'))
print(y.isdigit())



print("Del 3")‌‌ 
x = "a"

if(x in "APA"):
    print("Yes!")
else:‌‌ 
    print("No!")


if(x in "APA".lower()):‌‌ 
    print("Yes!")‌‌ 
else:‌‌ 
    print("No!")

x = "Kalle"
‌‌ 
if(x.count('l') >= 4):
    print("Yesss!")‌‌ 
elif x.count('e') > 0 and x.count('e') < 2:
    if(x.find('e') > 0 and x.find('e') < x.index(x[-1])):
        print("Middle letter!")
    else:‌‌ 
        print("Start or ending!")
        
else:‌‌ 
    print("Not that many...")

‌‌ 


print("Del 4")‌‌ 
x = 0‌‌ 
y = 25‌‌ 
‌‌ 
while x < y:‌‌ 
    print(x)‌‌ 
    x += 10‌‌ 
‌‌ 
‌‌ 
print("before loop:", x)
while x > 0:
‌‌    print(x)
    x -= 8

