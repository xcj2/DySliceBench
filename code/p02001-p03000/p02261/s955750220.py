import sys
from collections import namedtuple


class Card(namedtuple('Card', ('suit', 'value'))):
    __slots__ = ()

    def __str__(self):
        return self.suit + str(self.value)


def bubble_sort(cards):
    n = len(cards)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if cards[j - 1].value > cards[j].value:
                cards[j - 1], cards[j] = cards[j], cards[j - 1]


def selection_sort(cards):
    n = len(cards)
    for i in range(n):
        minj = min(range(i, n), key=lambda j: cards[j].value)
        if i != minj:
            cards[i], cards[minj] = cards[minj], cards[i]


cards = [Card(suit, value) for suit, value in sys.stdin.readlines()[1].strip().split()]

bubbled = cards[:]
bubble_sort(bubbled)
print(' '.join([str(c) for c in bubbled]))
print('Stable')

selected = cards[:]
selection_sort(selected)
print(' '.join([str(c) for c in selected]))
print('Stable' if selected == bubbled else 'Not stable')

