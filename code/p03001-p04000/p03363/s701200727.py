# def makelist(n, m):
#     return [[0 for i in range(m)] for j in range(n)]
import functools as ft

def permutation(n, k):
    if k > n:
        return 0
    elif 0 < k <= n:
        return ft.reduce(lambda x, y:x * y, [n - v for v in range(k)])
    else:
        return 1


def factorial(n):
    return permutation(n, n - 1)


def combination(n, k):
    return int(permutation(n, k) / factorial(k))

N = int(input())
A = [0] + list(map(int, input().split()))

for i in range(1, N):
    A[i+1] += A[i]

d = {}
for e in A:
    if e not in d:
        d[e] = 1
    else:
        d[e] += 1
ans = 0
for v in d.values():
    if v >= 2:
        ans += combination(v, 2)
print(ans)
