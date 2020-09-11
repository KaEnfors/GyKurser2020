import cards


DECK = cards.build_deck()


print("Prints all cards in list (deck)")
for CARD in DECK:
    cards.print_card(CARD)

print("Prints a randomly drawn card")
cards.print_card(cards.draw_card(DECK,True))


print("Prints a card drawn from the top")
cards.print_card(cards.draw_card(DECK))

cards.shuffle(DECK)
print("draw 1")
cards.print_card(cards.draw_card(DECK))
print("draw 2")
cards.print_card(cards.draw_card(DECK))
print("draw 3")
cards.print_card(cards.draw_card(DECK))
print("draw 4")
cards.print_card(cards.draw_card(DECK))