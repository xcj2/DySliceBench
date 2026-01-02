import sys


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


SENTINEL_NUM = 10 ** 9 + 1
cnt = 0
sentinel = Card(None, SENTINEL_NUM)


def merge(A, left, mid, right):
    global cnt
    global sentinel
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid] + [sentinel]
    R = A[mid:right] + [sentinel]

    i, j = 0, 0
    for k in range(left, right):
        cnt += 1
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def partition(A, p, r):
    x = A[r].value
    i = p - 1
    for j in range(p, r):
        if A[j].value <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


n = int(input())
A = [[None] * 2 for _ in range(n)]
B = [[None] * 2 for _ in range(n)]
for i in range(n):
    suit, value = input().split()
    A[i] = B[i] = Card(suit, int(value))

quick_sort(A, 0, n - 1)
merge_sort(B, 0, n)

if A == B:
    print("Stable")
else:
    print("Not stable")
for i in range(n):
    print(A[i].suit, A[i].value)

