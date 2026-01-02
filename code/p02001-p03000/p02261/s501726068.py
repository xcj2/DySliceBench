import copy


class Card:
    def __init__(self, pair):
        self.suit = pair[0]
        self.value = int(pair[1])

    def __str__(self):
        return self.suit + str(self.value)


def bubble_sort(a, n):
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if a[j].value < a[j-1].value:
                a[j], a[j-1] = a[j-1], a[j]


def selection_sort(a, n):
    for i in range(0, n):
        min_j = i
        for j in range(i, n):
            if a[j].value < a[min_j].value:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]


def equals(cards1, cards2):
    for card1, card2 in zip(cards1, cards2):
        if card1.suit != card2.suit:
            return False
    return True


def main():
    # input
    n = int(input())
    cards1 = list(map(Card, input().split(' ')))
    cards2 = copy.deepcopy(cards1)

    # sort
    bubble_sort(cards1, n)
    selection_sort(cards2, n)

    # output
    print(' '.join(map(str, cards1)))
    print('Stable')
    print(' '.join(map(str, cards2)))
    if equals(cards1, cards2):
        print('Stable')
    else:
        print('Not stable')


if __name__ == "__main__":
    main()

