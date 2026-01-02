def parent(i):
    return i//2

def left(i):
    return 2 * i

def right(i):
    return (2 * i) + 1

def maxHeapify(A, i):
    l = left(i)
    r = right(i)

    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <=n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in range(n//2, 0, -1):
        maxHeapify(A, i)
    
if __name__ == "__main__":
    n = int(input())
    A = [None]
    A.extend(list(map(int, input().split())))
    buildMaxHeap(A)
    print(" " + ' '.join(map(str, A[1:])))
