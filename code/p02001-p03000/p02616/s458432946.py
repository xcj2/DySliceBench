from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft



def main():
    n, k = map(int, input().split())
    a = sorted([(abs(i), (1 if i > 0 else -1)) for i in map(int, input().split())], reverse=True)
    if n == k:
        s = 1
        for x in a:
            s = s * x[0] * x[1] % mod
        print(s)
        return
    if len([i for i in a if i[1] == -1]) == n:
        if k % 2 == 0:
            s = 1
            for i in a[:k]:
                s = (s * i[0]) % mod
            print(s)
        else:
            s = 1
            for i in a[-k:]:
                s = (s * i[0]) % mod
            print((-s) % mod)
        return
    s = 1
    c = 1
    for i in range(k):
        s = s * a[i][0] % mod
        c *= a[i][1]
    if c == 1:
        print(s)
        return

    x_minus1 = -1
    x_plus1 = -1
    for i in range(k):
        if a[i][1] == -1:
            x_minus1 = a[i][0]
    for i in range(k, n):
        if a[i][1] == 1:
            x_plus1 = a[i][0]
            break

    x_minus2 = -1
    x_plus2 = -1
    for i in range(k):
        if a[i][1] == 1:
            x_minus2 = a[i][0]
    for i in range(k, n):
        if a[i][1] == -1:
            x_plus2 = a[i][0]
            break
    if x_minus1 == -1 or x_plus1 == -1:
        s = (s * inverse(x_minus2)) % mod * x_plus2 % mod
        print(s)
        return
    if x_minus2 == -1 or x_plus2 == -1:
        s = (s * inverse(x_minus1)) % mod * x_plus1 % mod
        print(s)
        return
    if x_plus1 * x_minus2 > x_plus2 * x_minus1:
        s = (s * inverse(x_minus1)) % mod * x_plus1 % mod
    else:
        s = (s * inverse(x_minus2)) % mod * x_plus2 % mod
    print(s)
main()
