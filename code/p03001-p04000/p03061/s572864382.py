#!/usr/bin/env python3

n = int(input())
a = [int(x) for x in input().split()]

m = 1
l = 0
while m < n:
    m *= 2
    l += 1
tr = [0] * (2 * m)

tr[m:m + n] = a


def gcd(a, b):
    if not a:
        return b
    while b:
        r = a % b
        a, b = b, r
    return a


def init_tr():
    for d in range(l - 1, -1, -1):
        for i in range(1 << d, 1 << (d + 1)):
            tr[i] = gcd(tr[i * 2], tr[i * 2 + 1])


def upd_tr(j):
    i = j // 2
    if i == 0:
        return
    tr[i] = gcd(tr[i * 2], tr[i * 2 + 1])
    upd_tr(i)


init_tr()

ans = 0

for i in range(n):
    tmp = tr[m + i]
    tr[m + i] = 0
    upd_tr(m + i)
    ans = max(ans, tr[1])
    tr[m + i] = tmp
    upd_tr(m + i)

print(ans)
