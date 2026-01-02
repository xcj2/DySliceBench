# coding:utf-8

import sys
import itertools

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, a, b, c = LI()
A = [a, b, c]
K = [II() for _ in range(n)]

ans = INF
for x in itertools.product([0, 1, 2, 3], repeat=n):
    s = set(x)
    if 0 not in s or 1 not in s or 2 not in s:
        continue
    T = [0] * 3
    cnt = 0
    for i, n in enumerate(x):
        if n == 3:
            continue
        if T[n]:
            cnt += 1
        T[n] += K[i]

    # print(T, cnt)
    tmp = cnt * 10
    for i in range(3):
        tmp += abs(T[i] - A[i])

    ans = min(ans, tmp)

print(ans)
