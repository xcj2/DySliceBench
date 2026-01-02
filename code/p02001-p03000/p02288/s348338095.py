KEY_MIN = -2000000001


H = int(input())

A = [KEY_MIN] * (H + 1)

for cnt, key in enumerate(map(int, input().split())):
    A[cnt + 1] = key

index_min = 1
index_max = len(A) - 1

def index_exsist(i):
    if index_min <= i <= index_max:
        return i
    else:
        return 0

def max_heapify(A, i):
    l = index_exsist(2 * i)
    r = index_exsist(2 * i + 1)

    largest = i
    if A[l] > A[largest]:
        largest = l
    if A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_maxheap(A):
    for i in range(1, (H // 2) + 1)[::-1]:
        max_heapify(A, i)


build_maxheap(A)
print("", *A[1:])

