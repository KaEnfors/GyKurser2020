# Detta program avrundar decimaltal till heltal
# Det blir dock fel avrundning. Vi vill att programmet ska avrunda uppåt.
# Exempelvis: 2.3 borde bli 2 men 2.5 borde bli 3
# Fixa...

A = int(input("Enter number A: "))
B = int(input("Enter number B: "))

RES = A / B
RES = int(RES)
print(A,"/",B,"=", RES)