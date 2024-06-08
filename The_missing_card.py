def missing_card(cards):
    colors = {"S", "H", "D", "C"}
    values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    fulldeck = {f"{color}{value}" for color in colors for value in values}
    
    fulldeck_set = set(fulldeck)
    missing_deck_set = set(cards.split())

    missing_card_found = fulldeck_set - missing_deck_set

    return missing_card_found.pop()


'''
Write a function named missing_card that given a card game returns the (single) missing card name.

The card game will be given as a single string of space-separated cards names.

A card is represented by its color and value, the color being in {"S", "H", "D", "C"} and the value being in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}, for a total of 52 possibilities.

You'll always be given 51 cards, and you have to return the missing one.
'''