import copy
INF = 10000000000
def Partition(A,p,r):
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            flag = 1
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def Qsort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        Qsort(A,p,q-1)
        Qsort(A,q+1,r)

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

N = int(input())
C = []
for i in range(N):
    C.append(input().split())
    C[i][1] = int(C[i][1])

D = copy.deepcopy(C)
Qsort(C,0,N-1)
mergeSort(D,0,N)

if C==D:
    print("Stable")
else:
    print("Not stable")
for i in range(N):
    print(C[i][0]+" "+str(C[i][1]))

