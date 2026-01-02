def maxheapify(A, i):
    l = 2 * i
    r = 2 * i + 1
    largest = -1

    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxheapify(A, largest)

def buildmaxheap(A):
    for i in reversed( range(1, int(  ( len(A) - 1 ) / 2.0 ) + 1 ) ):
        maxheapify(A, i)

def Main():
    n = int(input())
    A = [-1] + [ int(a) for a in input().split()]
    buildmaxheap(A)
    res = [" " + str(a) for a in A]
    print("".join(res[1:]))
    
Main()
