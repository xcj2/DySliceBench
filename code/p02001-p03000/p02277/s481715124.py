import copy
def partition(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def merge(A, left, mid, right):
    L = A[left:mid] + [[10000000000, 'S']]
    R = A[mid:right] + [[10000000000, 'S']]

    i = j = 0

    for k in range(left, right):
        if L[i][0] <= R[j][0]:
            A[k] = L[i]
            i += 1

        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
lstA = []
for i in range(n):
    C, N = input().split()
    k = [int(N), C]
    lstA.append(k)

lstB = copy.copy(lstA)
mergeSort(lstA, 0, n)
quicksort(lstB, 0, n-1)

if lstA == lstB:
    print('Stable')

else:
    print('Not stable')

for i in lstB:
    print(i[1], i[0])
