import copy

def swap(a, b):
    return b, a

def partition(A, p, r):
    x = int(A[r][1])
    i = p - 1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i = i+1
            A[i], A[j] = swap(A[i], A[j])
    A[i+1], A[r] = swap(A[i+1], A[r])
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
    return A

def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    L.append(['X', float('inf')])
    R.append(['X', float('inf')])
    i = 0
    j = 0
    for k in range(left, right):
        if float(L[i][1]) <= float(R[j][1]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def merge_sort(A, left, right):
    if left+1 < right:
        mid = (left + right) >> 1
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        return merge(A, left, mid, right)

def read_n_lows_input(n):
    Alist=[[j for j in input().split()] for i in range(n)]
    return Alist

n = int(input())
A = read_n_lows_input(n)
B = copy.deepcopy(A)
quick_sort(A, 0, n-1)
merge_sort(B, 0, n)
if A == B:
    print("Stable")
else:
    print("Not stable")
for i in A:
    print(*i, sep=" ")
