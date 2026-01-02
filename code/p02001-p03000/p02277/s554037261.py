import copy


n = int(input())
M = []
for _ in range(n):
    m = input().split()
    M.append([m[0], int(m[1])])

_M = copy.deepcopy(M)


def group(arr):
    r = {}
    for a in arr:
        if r.get(a[1]):
            r[a[1]] += a[0]
        else:
            r[a[1]] = a[0]

    return r


def partition(p, r):
    x = M[r][1]
    i = p - 1
    for k in range(p, r):
        if M[k][1] <= x:
            i += 1
            M[i], M[k] = M[k], M[i]
    M[i + 1], M[r] = M[r], M[i + 1]
    return i + 1


def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q - 1)
        quick_sort(q + 1, r)


quick_sort(0, n - 1)

if group(_M) == group(M):
    print('Stable')
else:
    print('Not stable')

for m in M:
    print(m[0], m[1])

