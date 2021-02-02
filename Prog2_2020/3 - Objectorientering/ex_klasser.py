"""
Exempel på klasser och hur man modellerar användbara
strukturer.

- Varför klasser?
    - Större program
    - Tydlighet i struktur
    - DRY, återanvändning
- Syntax för klasser
- Default-funktioner (init/string)
- Objekt vs Klass, vad är self?


"""







RANKS = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
]

SUITS = [
    "H",
    "S",
    "D",
    "C"
]

class Card():
    rank : int
    suit : int

    def __str__(self):
#        return str(self.__dict__)
        return SUITS[self.suit] + RANKS[self.rank]

    def higherThan(self, card):
        return self.rank > card.rank
        #if :
        #    return True
        ##else:
        # #   return False



class Deck():
    card : Card


mittkort = Card()
mittkort.rank = 0
mittkort.suit = 3

print(mittkort)

