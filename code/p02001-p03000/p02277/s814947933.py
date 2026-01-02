import math

def partition(A, p, r):
    x = A[r].num
    i = p
    for j in range(p, r):
        if x >= A[j].num:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i
    
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def merge(A, left, mid, right):
    L, R = [], []
    for a in A[left:mid]:
        L.append(a)
    for a in A[mid:right]:
        R.append(a)
    L.append(Card("dummy 0"))
    R.append(Card("dummy 0"))
    L[-1].num = math.inf
    R[-1].num = math.inf
    i, j = 0, 0
    for k in range(left, right):
        if L[i].num <= R[j].num:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if right - left > 1:
        mid = (right + left) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

class Card(str):
    def __init__(self, input_card):
        super().__init__
        self.num = int(input_card.split(" ")[-1])

N = int(input().rstrip())
A = []
for _ in range(N):
    A.append(Card(input().rstrip()))

A_2 = A.copy()

quickSort(A, 0, len(A)-1)
mergeSort(A_2, 0, len(A))

stable = True
for a_1, a_2 in zip(A, A_2):
    if a_1 != a_2:
        stable = False
        break
print("Stable" if stable else "Not stable")
for a in A:
    print(a)
