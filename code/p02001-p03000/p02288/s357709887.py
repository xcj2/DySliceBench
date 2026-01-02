# 最大ヒープ Maximum heap


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    largest = i
    if l <= H and A[l] > A[i]:
        largest = l
    if r <= H and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in range(H//2, 0, -1):
        maxHeapify(A, i)

H = int(input())
A = [-1] + [int(i) for i in input().split()]
buildMaxHeap(A)
for i in range(1, H+1):
    if i == H+1:
        print(A[i])
    else:
        print(" ", A[i], sep="", end="")
print()

