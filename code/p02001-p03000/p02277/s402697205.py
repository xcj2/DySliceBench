import copy

def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
        

def merge(A, left, mid, right):
    L = A[left:mid] + [("J", 1000000000) ]
    R = A[mid:right] + [("J", 1000000000)]
    i, j = 0, 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            
def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergesort(A, left, mid)
        mergesort(A, mid, right)
        merge(A, left, mid, right)
    
    
n = int(input())
A_Q = [input() for _ in range(n)]
A_Q = [(i.split()[0], int(i.split()[1])) for i in A_Q]
A_M = copy.deepcopy(A_Q)

quicksort(A_Q, 0, n-1)
mergesort(A_M, 0, n)

A_Q = [f"{str(i[0])} {str(i[1])}"for i in A_Q]
A_M = [f"{str(i[0])} {str(i[1])}"for i in A_M]
if A_Q == A_M:
    print("Stable")
else:
    print("Not stable")
print(*A_Q, sep="\n")

