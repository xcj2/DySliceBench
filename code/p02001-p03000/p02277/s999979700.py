# Quick Sort

N = int(input())
A = []
for _ in range(N):
    s, a = input().split()
    A.append((s, int(a)))

B = [a for a in A]


def partition(p, r):
    i = p-1
    x = A[r][1]
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i+1] = A[i+1], A[r]
    return i+1


def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)


INF = float('inf')


def merge(left, mid, right):
    L = B[left:mid]+[('sentinel', INF)]
    R = B[mid:right]+[('sentinel', INF)]
    l = 0
    r = 0

    for i in range(left, right):
        if L[l][1] <= R[r][1]:
            B[i] = L[l]
            l += 1
        else:
            B[i] = R[r]
            r += 1


def merge_sort(left, right):
    if left+1 < right:
        mid = (left+right)//2
        merge_sort(left, mid)
        merge_sort(mid, right)
        merge(left, mid, right)


quick_sort(0, N-1)
merge_sort(0, N)

print('Stable' if A == B else 'Not stable')
for s, v in A:
    print(s, v)


# print('Merge')
# for s, v in B:
#     print(s, v)

