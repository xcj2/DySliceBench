def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return int(i/2)

def maxHapify(A, i):
    l = left(i)
    r = right(i)
    largest = None
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHapify(A,largest)

def buildMaxHeap(A):
    for i in range(int(H/2),0, -1):
        maxHapify(A,i)
    

def printHeap(H,Q,n):
    if H+1 == n:
        return
    print("node",n,end=": ")
    print("key =",Q[n],end=", ")
    print("parent key =",Q[int(n/2)],end=", ") if 1<n else None
    print("left key =",Q[2*n],end=", ") if 2*n<=H else None
    print("right key =",Q[2*n+1],end=", ") if 2*n+1<=H else None
    print()
    printHeap(H,Q,n+1)
    



H = int(input())
Q = list(map(int, input().split()))
Q.insert(0,-1)
buildMaxHeap(Q)
print(end=" ")
print(" ".join(map(str,Q[1:])))


