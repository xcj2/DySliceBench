#クイックソート
import copy
 
INF = 10000000000
def merge(A, left, mid, right):
    count = 0
    L = A[left:mid] + [(INF,INF)]
    R = A[mid:right] + [(INF,INF)]
     
    i, j = 0, 0
    for k in range(left, right):
        count = count + 1
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return count
 
def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        countL = mergeSort(A, left, mid)
        countR = mergeSort(A, mid, right)
        return merge(A, left, mid, right) + countL + countR
    return 0

def partition(A, p, r):
    x = A[r][1]
    i = p
    for j in range(p, r):
        if A[j][1] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
        
        
    A[i], A[r] = A[r], A[i]
    
    return i

n = int(input())
A = [input().split() for _ in range(n)]
A = [(a[0], int(a[1])) for a in A]
B = [(a[0], int(a[1])) for a in A]

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
        
quickSort(A, 0, n-1)
mergeSort(B, 0, n)
if A == B:
    print('Stable')
else:
    print("Not stable")
    
ans = [str(a[0])+" "+str(a[1]) for a in A]
ans = '\n'.join(ans)
print(ans)

