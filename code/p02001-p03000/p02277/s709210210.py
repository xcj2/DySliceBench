from sys import stdin
from copy import deepcopy

INF = 1000000007

def partition(A, p, r):
    v = A[r]
    i = p
    for j in range(p, r):
        if A[j][1] <= v[1]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

# l <= m < rの範囲をマージ
def merge(A, l, m, r):
    L = A[l:m] + [("?", INF)]
    R = A[m:r] + [("?", INF)]
    li = 0
    ri = 0
    for j in range(l, r):
        if L[li][1] <= R[ri][1]:
            A[j] = L[li]
            li += 1
        else:
            A[j] = R[ri]
            ri += 1

def mergeSort(A, l, r):
    if r-l > 1:
        mid = l + (r-l)//2
        mergeSort(A, l, mid)
        mergeSort(A, mid, r)
        merge(A, l, mid, r)

def isStable(A, sorted_A):
    stable_A = deepcopy(A)
    mergeSort(stable_A, 0, len(stable_A))
    for i in range(len(A)):
        if stable_A[i] != sorted_A[i]:
            return False

    return True

n = int(stdin.readline().rstrip())
cards = []
for _ in range(n):
    s, num = stdin.readline().rstrip().split()
    cards.append((s, int(num)))

sorted_cards = deepcopy(cards)
quicksort(sorted_cards, 0, n-1)
if isStable(cards, sorted_cards):
    print("Stable")
else:
    print("Not stable")

for card in sorted_cards:
    print(*card)

