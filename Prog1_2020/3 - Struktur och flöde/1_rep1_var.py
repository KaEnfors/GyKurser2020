"""
Variabler typer och beräkningar
"""

‌‌ 

‌‌ 
x‌‌ = 25
y = 11‌‌ 
c = x % y

print(x+y)       #36
print(c + y % c) #
print(x % c + y)



‌‌ 


x = "Donald"
y = "Trump"
‌‌ 
print(x*5) 
print(y*5)‌‌ 
print((x + y)‌‌ * 5)
print(x[0]*5 + x,y + y[-1]*5)

print((x*5).count('o'))
print( (x + " " + y).count('r') )
‌‌ 
x = "No ordinary brain exersize".split()
y = x[0]‌‌ 
y +=‌‌ x[1][0]
y += x[2][0]
z = x[3].index('s')
y += (x[3][z])
print(y.lower().startswith('n'), y)
‌‌ 





x = 2‌‌ 
y = 7‌‌ 

x = y - x‌‌ 
y = x + y%x‌‌ 
x *= 2‌‌ 
y -=x‌‌ 
x += y + x - (y + x)*2*(5%3-3)
print(x)
print(y)‌‌ 
‌‌
