import copy

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def equals(self, card):
        if (card.suit == self.suit) and (card.number == self.number):
            return True
        else:
            return False

def bubble_sort(cards, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if cards[j - 1].number > cards[j].number:
                cards[j - 1], cards[j] = cards[j], cards[j - 1]
    return cards

def selection_sort(cards, n):
    for i in range(n):
        min_j = i
        for j in range(i, n):
            if cards[j].number < cards[min_j].number:
                min_j = j
        if min_j != i:
            cards[i], cards[min_j] = cards[min_j], cards[i]
    return cards

def is_stable(cards1, cards2, n):
    result = True
    for i in range(n):
        if not(cards1[i].equals(cards2[i])):
            result = False
            break
    return result

def print_cards(cards, n):
    print(' '.join([c.suit + str(c.number) for c in cards]))

n = int(input())
cards = [Card(card[0], int(card[1])) for card in input().split()]
cards_bubble = bubble_sort(copy.deepcopy(cards), n)
cards_selection = selection_sort(copy.deepcopy(cards), n)

print_cards(cards_bubble, n)
print('Stable')
print_cards(cards_selection, n)
if is_stable(cards_bubble, cards_selection, n):
    print('Stable')
else:
    print('Not stable')

