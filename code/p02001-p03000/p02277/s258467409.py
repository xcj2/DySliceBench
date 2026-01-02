import sys

class Card:
    def __init__(self, s, n, i):
        self.suit = s
        self.num = n
        self.ini_ord = i

def is_stable(A, n):
    for i in range(n - 1):
        if A[i].num == A[i + 1].num:
            if A[i].ini_ord > A[i + 1].ini_ord:
                return False

    return True

def partition(A, p, r):
    x = A[r].num
    i = p - 1

    for j in range(p, r):
        if A[j].num <= x:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[i + 1] , A[r] = A[r], A[i + 1]

    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

n = int(sys.stdin.readline().rstrip())
cards = []

for i in range(n):
    line = sys.stdin.readline().split()
    cards.append(Card(line[0], int(line[1]), i))

quickSort(cards, 0, n - 1)

if is_stable(cards, n):
    print("Stable")
else:
    print("Not stable")

for i in range(n):
    print(cards[i].suit,str(cards[i].num))