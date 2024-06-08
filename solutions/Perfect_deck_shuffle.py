def perfect_shuffle(deck):
    left = []
    right = []
    fin_deck =[]

    split_num = len(deck) / 2
    count = 0
    for card in deck:
        if count < split_num:
            left.append(card)
            count += 1
        else:
            right.append(card)

    count = 0
    try:
        while count < len(left) or count < len(right):
                fin_deck.append(left[count])
                fin_deck.append(right[count])
                count += 1
    except IndexError:    
        return fin_deck
    return fin_deck


deck = [1,2,3,4,5,6,7]
print(perfect_shuffle(deck))


'''


Simulate a perfect suffle of a deck of cards.

A perfect shuffle of a deck of card is splitting a deck of cards into equal halves, and perfectly interleaving them.

Perfectly shuffling [1, 2, 3, 4, 5, 6] gives [1, 4, 2, 5, 3, 6].

(We consider that a deck of cards has an even number of cards.)

You'll expose a perfect_shuffle(deck) function, perfectly shuffling the given iterable.

Did you know that if you shuffle 10 times a deck of 1024 cards, the deck returns to its initial state ? It's probably a good way to test your implementation.


'''