## Quick Sort

import copy

N = int(input())
lst1 = [list(input().split()) for i in range(N)]
lst2 = copy.copy(lst1)
INF = 10**9 + 1

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid]
    L.append(("", INF))  # 番兵
    R = A[mid:right]
    R.append(("", INF))  # 番兵
    i, j = 0, 0
    for k in range(left, right):
        if (int(L[i][1]) <= int(R[j][1])):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, left, right):
    if (right - left > 1):
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)
        
def partition(A, p, r):
    x = int(A[r][1])
    i = p - 1
    for j in range(p, r):
        if (int(A[j][1]) <= x):
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

quick_sort(lst1, 0, N-1)
merge_sort(lst2, 0, N)
ans = 'Stable'
if (lst1 != lst2):
    ans = 'Not stable'
print(ans)
for i in lst1:
    print(*i)

