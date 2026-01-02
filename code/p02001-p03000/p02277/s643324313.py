N = int(input())
A1 = []
A2 = []
for _ in range(N):
    a = input().split()
    A1.append((a[0], int(a[1])))
    A2.append((a[0], int(a[1])))

snt = 10 ** 9 + 1

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x[1]:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def merge(A, left, mid, right):
    L = A[left:mid] + [('SNT', snt)]
    R = A[mid:right] + [('SNT', snt)]
    i, j = 0, 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

quick_sort(A1, 0, N - 1)
merge_sort(A2, 0, N)

print('Stable' if A1 == A2 else 'Not stable')
for a1 in A1: print(*a1)
