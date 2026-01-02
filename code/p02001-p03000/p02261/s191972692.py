
class Card:
    def __init__(self, data, i):
        self.suit = data[0]
        self.value = data[1]
        self.initord = i

def BubbleSort(cards, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if cards[j].value < cards[j - 1].value:
                cards[j], cards[j - 1] = cards[j - 1], cards[j]

def SelectionSort(cards, N):
    for i in range(N):
        min_j = i

        for j in range(i + 1, N):
            if cards[j].value < cards[min_j].value:
                min_j = j

        cards[i], cards[min_j] = cards[min_j], cards[i]

N = int(input())
cards = [Card(data, i) for i, data in enumerate(input().split())]

cards1 = cards.copy()
cards2 = cards.copy()

BubbleSort(cards1, N)
SelectionSort(cards2, N)

print(*[card.suit + card.value for card in cards1])

for i in range(N - 1):
    if cards1[i].value == cards1[i + 1].value:
        if cards1[i].initord > cards1[i + 1].initord:
            print("Not stable")
            break
else:
    print("Stable")

print(*[card.suit + card.value for card in cards2])

for i in range(N - 1):
    if cards2[i].value == cards2[i + 1].value:
        if cards2[i].initord > cards2[i + 1].initord:
            print("Not stable")
            break
else:
    print("Stable")