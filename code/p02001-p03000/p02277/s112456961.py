class Card(object):
    def __init__(self, *data):
        self.chr, self.num = data
        self.num = int(self.num)
        self.chr = str(self.chr)


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j].num <= x.num:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def merge(A, left, mid, right):
    L = A[left:mid] + [Card('A', 10**10)]
    R = A[mid:right] + [Card('A', 10**10)]
    i = 0
    j = 0
    # 右と左比べて小さい方をとってくる
    for k in range(left, right):
        if L[i].num <= R[j].num:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


# マージソートとクイックソート比べる
n = int(input())
A = [Card(*(input().split())) for _ in range(n)]
B = A[:]
C = A[:]

quicksort(B, 0, n-1)
mergeSort(C, 0, n)
flag = True
for b, c in zip(B, C):
    if b is not c:
        flag = False
        break
if flag:
    print('Stable')
else:
    print('Not stable')

for i in range(n):
    print(B[i].chr, B[i].num)
