H = int(input())
B = [int(i) for i in input().split()]

def left(i):
    return i*2

def right(i):
    return i*2 + 1

def maxHeapify(A, i):
    H = len(A)
    l = left(i)
    r = right(i)
    if l <= H and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= H and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        A = maxHeapify(A, largest)
    return A

def buildMaxHeap(A):
    H = len(A)
    for i in range(H//2, 0, -1):
        A = maxHeapify(A,i)
    return A

A = buildMaxHeap(B)
print("", *A)
