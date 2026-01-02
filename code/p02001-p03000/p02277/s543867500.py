import sys
from enum import IntEnum
from collections import defaultdict

def partition(li, p, r): 
    """Separate li with a value of li[r].
    Returns index of the partition value.

    >>> ax = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    >>> partition(ax, 0, 11)
    7
    >>> ax
    [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]
    """
    x = li[r]
    i = p - 1 
    for j in range(p, r): 
        if li[j] <= x:
            i += 1
            li[i], li[j] = li[j], li[i]

    i += 1
    li[i], li[r] = li[r], li[i]

    return i


def quicksort(li, p, r):
    """sort li by quick sort algorithm.

    >>> li = [3, 2, 1, 3, 2, 1]
    >>> quicksort(li, 0, 5)
    >>> li
    [1, 1, 2, 2, 3, 3]
    """
    if p < r:
        q = partition(li, p, r)
        quicksort(li, p, q-1)
        quicksort(li, q+1, r)


def is_stable(target, original):
    """Returns true if the target list is keeps
    the order of the original list.
    Assumes that the target list is sorted.

    >>> a = Card('H', 2)
    >>> b = Card('D', 2)
    >>> org = [a, b]
    >>> tg1 = [b, a]
    >>> is_stable(tg1, org)
    False
    >>> tg2 = [a, b]
    >>> is_stable(tg2, org)
    True
    """

    size = len(original)
    orgstack = defaultdict(list)
    trgstack = defaultdict(list)

    for i in range(size):
        orgstack[original[i].number].append(original[i])
        trgstack[target[i].number].append(target[i])

    for num in orgstack.keys():
        org = orgstack[num]
        trg = trgstack[num]
        if len(org) != len(trg):
            return False

        while len(org) > 0:
            if not org.pop() is trg.pop():
                return False

    return all([len(v) == 0 for k, v in trgstack.items()])


class Suit(IntEnum):
    S = 1
    H = 2
    D = 3
    C = 4


class Card:
    def __init__(self, suit, number):
        assert 1 <= number <= 10**9

        self.suit = Suit[suit]
        self.number = number

    def __eq__(self, other):
        """check object has the same value.

        >>> a = Card('H', 1)
        >>> b = Card('D', 1)
        >>> a == b
        True
        """
        return self.number == other.number

    def __gt__(self, other):
        return self.number > other.number

    def __lt__(self, other):
        return self.number < other.number

    def __ge__(self, other):
        return (self.number == other.number
                or self.number > other.number)

    def __le__(self, other):
        return (self.number == other.number
                or self.number < other.number)

    def __hash__(self):
        """check object is identical.

        >>> a = Card('H', 1)
        >>> b = Card('D', 1)
        >>> a is b
        False
        """
        return hash(self.suit, self.number)

    def __str__(self):
        return '{} {}'.format(self.suit.name, self.number)


def run():
    count = int(input())  # flake8: noqa
    cards = []
    for line in sys.stdin:
        s, n = line.split()
        cards.append(Card(s, int(n)))

    sorted_cards = cards[:]
    quicksort(sorted_cards, 0, count-1)

    if is_stable(sorted_cards, cards):
        print('Stable')
    else:
        print('Not stable')

    for c in sorted_cards:
        print(c)


if __name__ == '__main__':
    run()
