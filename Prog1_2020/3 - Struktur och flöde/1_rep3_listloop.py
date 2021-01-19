"""
Listor

"""



x = ["1", "2", "3"]
x.append("4")
x.append("5")

print(x[3])
print(x[0])
print(x[-1])
print(x[-3])
print(x[2:4])
print(x[0:2])
print(x[2:5])

print(x.index("1"))
print(x.index("5"))
print(len(x))

x = [3,8,6,1,2]

for item in x:
    print(item % 2)


print("del2")

y = []

for i in range(1,len(x),1):
    print(x[i-1])
    z = x[i-1] + x[i]
    y.append(z)
    if z > 7:
        y[len(y)-1] += 10
    else:
        y[0] += 2
        
    print(y)



print("del3")

for a in range(0,10,2):
    for b in range(0,10,3):
        print(a*b)



print("del3")
def con(z):
    return z**2
i = 2
while not con(i) > 20:
    i = con(i)

print("?:", i)