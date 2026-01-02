class card:
    def __init__(self, card):
        self.suit = card[0]
        self.value = int(card[1])

    def __repr__(self):
        return self.suit + str(self.value)


def selectionSort(a, n):
    r = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j].value < a[minj].value:
                minj = j
        a[i], a[minj] = a[minj], a[i]


def bubbleSort(a, n):
    flag = True
    while flag:
        flag = False
        for j in range(n - 1, 0, -1):
            if a[j].value < a[j - 1].value:
                a[j], a[j - 1] = a[j - 1], a[j]
                flag = True


def copycard(cards):
    r = []
    for c in cards:
        r.append(card(c.suit + str(c.value)))
    return r


def compareCard(c1,c2):
    for i in range(len(c1)):
        if c1[i].suit != c2[i].suit or c1[i].value != c2[i].value:
            return False
    return True


n = int(input())
cards = list(map(card, input().split()))
cards1 = copycard(cards)
cards2 = copycard(cards)
bubbleSort(cards1, n)
print(*cards1)
print("Stable")
selectionSort(cards2, n)
print(*cards2)
if compareCard(cards1,cards2):
    print("Stable")
else:
    print("Not stable")


