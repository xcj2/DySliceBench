class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + self.value


N = int(input())
cards1 = [Card(card[0], card[1]) for card in list(map(str, input().split()))]
cards2 = [*cards1]


def bubbleSort(cards: list, n: int):
    for i in range(n):
        for j in reversed(range(i+1, n)):
            if cards[j-1].value > cards[j].value:
                cards[j-1], cards[j] = cards[j], cards[j-1]
    return cards


def selectionSort(cards: list, n: int):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if cards[minj].value > cards[j].value:
                minj = j
        cards[i], cards[minj] = cards[minj], cards[i]
    return cards


def isStable(cards1: list, cards2: list, n: int):
    for i in range(n):
        if cards1[i].suit != cards2[i].suit:
            return False
    return True


bubbleSort(cards1, N)
selectionSort(cards2, N)
print(*cards1)
print('Stable')
print(*cards2)
print('Stable' if isStable(cards1, cards2, N) else 'Not stable')

