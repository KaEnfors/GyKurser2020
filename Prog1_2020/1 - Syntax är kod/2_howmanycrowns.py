"""
Ett program som räknar ut hur många svenska 
kronor, ett antal dollar eller euro har

"""

print("###################################")
print("Calculate number of swedish crowns")
print("from Euros or Dollars")
print("###################################")

VALUE_OF_DOLLAR = 8.77              #Värdet på dollar sparas i en konstant variabel
VALUE_OF_EURO = 10.36               #Värdet på euro sparas i en konstant variabel

value = input("Enter amount, end with $ or €\n: ") #Användaren skriver in mängden
print("You entered:", value)        #Det användaren skrev in, skrivs ut som bekräftelse

if(value[-1] == '$'):               #Om sista bokstaven är ett dollartecken, då räknar vi dollar...
    dollars = int(value[:-1])
    crowns = dollars * VALUE_OF_DOLLAR
else:                               #...Annars räknar vi på euro
    euros = int(value[:-1])
    crowns = euros * VALUE_OF_EURO

print(value, "is", crowns, "kr")    #Resultatet skrivs ut
