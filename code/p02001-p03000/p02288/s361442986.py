import math


def max_heapify(A, n, i):
    largest = most_largest(A, n, i)
    x = i
    while largest is not x:
        tmp = A[x]
        A[x] = A[largest]
        A[largest] = tmp
        x = largest
        largest = most_largest(A, n, x)


def most_largest(A, n, i):
    l = left(i)
    r = right(i)
    largest = None
    if l <= n and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r <= n and A[largest] < A[r]:
        largest = r
    return largest


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return math.floor(i / 2)


def build_max_heap(A, n):
    for i in range(math.floor(n/2), 0, -1):
        max_heapify(A, n, i)


n = int(input())
heap = [None] + list(map(int, input().split()))

build_max_heap(heap, n)

print(' ', end='')
print(*heap[1:])

