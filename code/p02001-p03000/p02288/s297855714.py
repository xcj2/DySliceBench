def left(i:int):
    return i * 2

def right(i:int):
    return i * 2 + 1

def maxHeapify(A:list, i:int):
    l = left(i)
    r = right(i)
    global H
    if l <= H  and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H  and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapify(A, largest)

def buildMaxHeap(A:list):
    global H
    for i in range(int(H/2), 0, -1):
        maxHeapify(A, i)

H = int(input())
A = [None]
A.extend(list(map(int,input().split())))
buildMaxHeap(A)
print(" ", end="")
print(*A[1:])
