def partition(A,p,r):
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    

def stable(A,Q):
    for i in range(1,len(Q)):
        if int(Q[i-1][1]) == int(Q[i][1]):
            x = A.index(Q[i-1])
            y = A.index(Q[i])
            if y<x:
                return 'Not stable'
    return 'Stable'

n = int(input())
A = []
for i in range(n):
    a = input().split()
    a[1]=int(a[1])
    A.append(a)
Q = A.copy()
quicksort(Q, 0, n-1)
print(stable(A,Q))
for i in range(len(Q)):
    print(Q[i][0], Q[i][1])
