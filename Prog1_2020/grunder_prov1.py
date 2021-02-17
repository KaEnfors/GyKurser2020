
x = 31
y = 15
c = x % y 

print("1", x+y) #46 
print("2", c + (y % c)) # 1
print("3", (x % c) + y) # 15



x = "Joe"
y = "Biden"

print("4", y*2) # "BidenBiden"
print("5",   'Y'*5 + x  ,  y + y[-1]*5   ) #YYYYYJoe Bidennnnnn

print("6", (x*5).count('o')) #5
print("7", (x + " " + y).count('r') ) #"Joe Biden" -> 0




x = "I will write potato in the chat"
y = x[0] # y="I"
y += x[-1] #y="It"     x[-3] = h     x[-7] = h     x[ 5 % 2 ] = " "
y += x[5] #y="Itl"
z = x.index('w') #z=2
y += (x[3]) #y= "Itli"
print("8", y.lower()) #"itli"



def woop(n, inc):
    #n=0, inc=-1
    return n + inc #-1

i = 0

while i > -20: #0, -1, -2...-14...-19
    i = woop(i, -1) #-20
    
print("9", i) # -20



x = 'a'
if(x in "APA"): #False (a != A)
    print("10", "gurka!")
else:
    print("10", "ingen gurka!")


x = "Python is awesome".count('o') # x = 2
if ((x > 10) or (x < 3)): #True
    x *= "or is it?".count('i') # x = 2 * 2
    if x > 0 and x < 20:
        print("11", "Yep!") #!!!!!!!!
    else:
        print("11", "Nope!") # ---
else:
    print("11", "Def. nope!!") #---


x = 4
y = ""
while (x%9 != 0): # Igor, Marino, Rami, Michael, Mohammed, Adnoay, Elias är ni här? False
    x += 8 # x = 36
    y +=  str(x) + "," #y= "12,20,28,36"
print("12", y) # "12,20,28,36"

#Igor Marino, Atakan, Elias, Simon, är ni här? Skriv potatis!!

# Igor, Marino, Tjalve, Michael, Atakan, Elias, Mahad, Mohammed, Rami Skriv gurka!
x = 0
for a in range(0,5,2): # rangen = [0,2,4] 
    for b in range(0,8,3): # rangen = [0,3,6] 
        x += b #x = 27
print("13", x) # 27
#Frågor? Reza, JKulian, Mahad, Daniel, Igor, Marino, Elias, Sahil, Mohammed, 
#Zahid är ni här? Skriv tomat!


def con(z): #z = 2
    return z**2 # 4*4
    
i = 2
while not con(i) > 20: # Fasle
    i = con(i) #16

print("14:", i) #16

#Skriv snögubbe!!!!!
