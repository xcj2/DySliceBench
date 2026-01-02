n = int(input())
A = [int(i) for i in input().split()]

def parent(i):
    i += 1
    return int(i/2) -1

def left(i):
    i += 1
    return 2*i -1

def right(i):
    i += 1
    return 2*i + 1 -1

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    
    largest = i
    if(l < len(A) and A[l] > A[i] ):
        largest = l
    
    if(r < len(A) and A[r] > A[largest]):
        largest = r
    
    if(largest != i):
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)
#         print(A)
    
    return A
        
def buildMaxHeap(A):
    for i in range(int(len(A)/2)-1, -1, -1):
        A = maxHeapify(A, i)
    return A

A = buildMaxHeap(A)

print(" {}".format(" ".join([str(i) for i in A])))
