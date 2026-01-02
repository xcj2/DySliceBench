class Card:
    def __init__(self, label):
        suits = ['S', 'H', 'C', 'D']
        suit, value = list(label)
        assert(suit in suits and 0 < int(value) < 10)

        self.suit = suit
        self.value = int(value)

    def __eq__(self, other):
        """equal

        >>> Card('S1') == Card('D9')
        False
        >>> Card('D9') == Card('S1')
        False
        >>> Card('C5') == Card('C5')
        True
        """
        return self.value == other.value

    def __lt__(self, other):
        """less than

        >>> Card('S1') < Card('D9')
        True
        >>> Card('D9') < Card('S1')
        False
        """
        return self.value < other.value

    def __gt__(self, other):
        """greater than

        >>> Card('S1') > Card('D9')
        False
        >>> Card('D9') > Card('S1')
        True
        """
        return self.value > other.value

    def __hash__(self):
        return hash((self.suit, self.value))

    def __str__(self):
        return self.suit + str(self.value)


def bubble_sort(deck):
    """sort deck by bubble sort

    >>> deck = [Card('H4'), Card('C9'), Card('S4'), Card('D2'), Card('C3')]
    >>> print(" ".join([str(c) for c in bubble_sort(deck)]))
    D2 C3 H4 S4 C9
    """
    size = len(deck)
    for i in range(size):
        for j in reversed(range(i+1, size)):
            if deck[j] < deck[j-1]:
                deck[j-1], deck[j] = deck[j], deck[j-1]

    return deck


def selection_sort(deck):
    """sort deck by selection sort

    >>> deck = [Card('H4'), Card('C9'), Card('S4'), Card('D2'), Card('C3')]
    >>> print(" ".join([str(c) for c in selection_sort(deck)]))
    D2 C3 S4 H4 C9
    """
    size = len(deck)
    for i in range(size):
        mini = i
        for j in range(i, size):
            if deck[mini] > deck[j]:
                mini = j
        deck[i], deck[mini] = deck[mini], deck[i]

    return deck


def is_stable_sorted(org, deck):
    """check if deck is sorted by stable manner

    >>> c1 = Card('S1')
    >>> c2 = Card('D1')
    >>> is_stable_sorted([c1, c2], [c1, c2])
    True
    >>> is_stable_sorted([c1, c2], [c2, c1])
    False
    """
    idx = {c:i for (i, c) in enumerate(org)}
    return all([c1 < c2 or idx[c1] < idx[c2]
                for (c1, c2) in zip(deck[:-1], deck[1:])])


def check_stable(org, deck):
    if is_stable_sorted(org, deck):
        return "Stable"
    else:
        return "Not stable"


def run():
    _ = int(input()) # flake8: noqa
    deck = []
    for lb in input().split():
        deck.append(Card(lb))

    db = bubble_sort(deck[:])
    print(" ".join([str(c) for c in db]))
    print(check_stable(deck, db))

    ds = selection_sort(deck[:])
    print(" ".join([str(c) for c in ds]))
    print(check_stable(deck, ds))


if __name__ == '__main__':
    run()

