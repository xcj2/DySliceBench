count = 0

#クイックソート
def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            a = A[j]
            A[j] = A[i]
            A[i] = a
    a = A[i+1]
    A[i+1] = A[r]
    A[r] = a

    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

#比較のための安定なソートとしてのマージソート
def merge(a, left, mid, right):
    global count
    L = [0] * (mid - left + 1)
    R = [0] * (right - mid + 1)

    for i in range(len(L)):
        if i  == len(L) - 1:
            L[i] = ['A', float('inf')]
        else:
            L[i] = a[left+i]
    
    for i in range(len(R)):
        if i == len(R) - 1:
            R[i] = ['A', float('inf')]
        else:
            R[i] = a[mid+i]

    i = 0
    j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            a[k] = L[i]
            i += 1
        else:
            if i != len(L) - 1 and j != len(R) - 1:
                count += len(L) - i - 1
            a[k] = R[j]
            j += 1

def mergeSort(a, left, right):
    if left+1 < right:
        mid = int((left + right) / 2)
        mergeSort(a, left, mid)
        mergeSort(a, mid, right)
        merge(a, left, mid, right)

n = int(input())
A = []
A2 = []
for i in range(n):
    cell = input().split()
    A.append([cell[0], int(cell[1])])
    A2.append([cell[0], int(cell[1])])

quicksort(A, 0, n-1)
mergeSort(A2, 0, n)

flag = 0
for i in range(n):
    if A[i] != A2[i]:
        flag = 1

if flag == 1:
    print('Not stable')
else:
    print('Stable')

for i in range(n):
    print(str(A[i][0]) + ' ' + str(A[i][1]))
