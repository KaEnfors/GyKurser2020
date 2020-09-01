import matplotlib.pyplot as graph
import numpy as math



x = math.linspace(-10, 10, 100)  # Skapa punkter längs x-axeln. Grafen börjar på 0, slutar på 20 och ska ha 100 punkter
#print(x)                       # Printa innehållet i x, så ser du 100 punkter med jämna mellanrum
#graph.plot(x, math.sin(x))     # Rita funktionen y = sin(x)
graph.plot(x, x*x)           # Rita y = kx + m
#graph.plot(x, -1.2*x-2)         # Rita y = kx + m
#graph.plot(x, 2*x+-2)           # Rita y = kx + m
#graph.plot(x, 0.3*x+1)          # Rita y = kx + m


#
# 1. Grafer, med + * - /
# 2. Testa med ** (exponentiering)
# 3. Testa floor division //  ... 5//2 = ?
# 4. Modulo (%)
#
#


graph.axhline(0, color='gray')
graph.axvline(0, color='gray')
graph.grid()


graph.show()                   # Visa grafen



