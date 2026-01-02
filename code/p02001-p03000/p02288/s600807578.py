import sys
def input():
    return sys.stdin.readline()[:-1]

H = int(input())
A = list(map(int, input().split()))

def maxHeapify(A, i):
    c = i
    l = 2*(i+1)-1 if 2*(i+1)<=H  else H+1
    r = 2*(i+1)+1-1 if 2*(i+1)+1<=H else H+1 

    # select maximum node from left, me, right
    if (l<=H) and (A[l]>A[c]):
        largest = l
    else:
        largest = c
    if (r<=H) and (A[r]>A[largest]):
        largest = r
        
    if largest!=c:
        A[c],A[largest] = A[largest],A[c]
        if 2*(largest+1)<=H:
            maxHeapify(A, largest)
    return A

def buildMaxHeap(A):
    for i in range(H//2-1, -1, -1):
        A = maxHeapify(A,i)
        
buildMaxHeap(A)
print(' '+' '.join([str(a) for a in A]))
