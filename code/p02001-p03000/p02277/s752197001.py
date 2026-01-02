import copy

n = int(input())
A = []
for i in range(n):
    tmp = input().split()
    A.append([tmp[0], int(tmp[1])])
B = copy.deepcopy(A)

# ===========================================================================

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

# ============================================================================
# merge sort (for comparison)

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = ['nan', float("inf")]
    R[n2] = ['nan', float("inf")]
    i = 0
    j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            
def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


# ============================================================================
quick_sort(A, 0, len(A)-1)
merge_sort(B, 0, len(B))

print('Stable' if A == B else 'Not stable')
for x in A:
    print(x[0] + ' ' + str(x[1]))

