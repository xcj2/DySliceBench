# Quick sort クイックソート


class Card():

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
    
    def __repr__(self):
        return str(self.suit) + " " + str(self.num)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j].num <= x.num:
            i += 1
            t = A[i]
            A[i] = A[j]
            A[j] = t
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def mergesort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergesort(A, left, mid)
        mergesort(A, mid, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    i1, i2 = 0, 0
    L = A[left:mid] + [Card("X", 2000000000)]
    R = A[mid:right] + [Card("X", 2000000000)]
    for j in range(left, right):
        if L[i1].num <= R[i2].num:
            A[j] = L[i1]
            i1 += 1
        else:
            A[j] = R[i2]
            i2 += 1


def compareCards(c1, c2):
    return c1.suit == c2.suit and c1.num == c2.num


def compareStacks(A, B):
    for i in range(len(A)):
        if not compareCards(A[i], B[i]):
            return False
    return True


n = int(input())
A, B = [], []
for i in range(n):
    suit, num = input().split()
    A += [Card(suit, int(num))]
    B += [Card(suit, int(num))]
quicksort(A, 0, n - 1)
mergesort(B, 0, n)
if compareStacks(A, B):
    print("Stable")
else:
    print("Not stable")
for a in A:
    print(a)

