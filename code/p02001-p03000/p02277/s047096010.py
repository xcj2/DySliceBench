# import sys
# sys.stdin = open('input.txt', 'r')

class Card:
    def __init__(self):
        self.suit = ''
        self.num = 0
    def __str__(self):
        return self.suit + ' ' + str(self.num)

def merge(A, left, mid, right):
    """
    right: 最後の添字 + 1
    """
    SENTINEL = Card()
    SENTINEL.num = 2 * 10**9

    n1 = mid - left;
    n2 = right - mid;
    L = A[left:left+n1]
    R = A[mid:mid+n2]

    L.append(SENTINEL)
    R.append(SENTINEL)
    i = 0
    j = 0

    for k in range(left, right):
        if L[i].num <= R[j].num:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2;
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

def partition(A, p, r):
    """
    r: 最後の添字
    """
    x = A[r].num # last item
    i = p - 1
    for j in range(p, r):
        if A[j].num <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1 # index of the initial A[r]

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

n = int(input())
A = []
for i in range(n):
    x = Card()
    x.suit, x.num = input().split()
    x.num = int(x.num)
    A.append(x)

A_mergeSort = A[:]
mergeSort(A_mergeSort, 0, n)
quickSort(A, 0, n-1)
isStable = True

for i in range(n):
    if A[i].suit == A_mergeSort[i].suit and A[i].num == A_mergeSort[i].num:
        pass
    else:
        isStable = False

print('Stable') if isStable else print('Not stable')

for i in A:
    print(i)
