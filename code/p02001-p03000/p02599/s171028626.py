#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def bit_add(a, i, n, x):
    while i < n:
        a[i] += x
        i += i & -i
def bit_add2(a, i, j, n, x):
    if j<<1 < n:
        n = 1 << j.bit_length()
    while i < n:
        a[i] += x
        i += i & -i
    while j < n:
        a[j] -= x
        j += j & -j

def bit_sum(a, i):
    res = 0
    while i > 0:
        res += a[i]
        i ^= i & -i
    return res

def resolve():
    it = map(int, sys.stdin.read().split())
    N, Q = next(it), next(it)
    X = Q.bit_length()
    mask = (1 << X)-1

    Aa = [next(it)-1 for i in range(N)]
    Aq = [0] * Q
    Ac = [0] * Q
    for i in range(Q):
        l, r = next(it), next(it)
        Aq[i] = r<<X | i
        Ac[i] = l

    Aq.sort()
    dp = [1] * N
    N1 = N+1
    bit = [0] * N1

    ans = [0] * Q
    offset = 0
    for arg in Aq:
        r = arg >> X
        i = arg & mask

        for j in range(offset, r):
            ci = Aa[j]
            j += 2

            j0 = dp[ci]
            bit_add2(bit, j0, j, N1, 1)

            dp[ci] = j

        offset = r
        l = Ac[i]

        ans[i] = bit_sum(bit, l)

    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()
