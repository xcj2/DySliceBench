
n = int(input())

a = list(map(int, input().split()))
a.sort(reverse=True)


from functools import lru_cache
import sys
if n == 2:
    print(max(a))
    sys.exit()


@lru_cache(maxsize=100000)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def gcd_list(li):
    if len(li) == 1:
        return li[0]
    g = gcd(li[0], li[1])
    for i in range(2, len(li)):
        g = gcd(g, li[i])
    return g


def gcd_list_2(li):
    g = gcd(li[0], li[1])
    if g == 1:
        return max(gcd_list([li[0]] + li[2:]), gcd_list(li[1:]))
    for i in range(2, n):
        if gcd(g, li[i]) == 1:
            if i == n - 1:
                return gcd_list(li[:i])
            gg = gcd_list(li[i+1:])
            bb = [gcd(li[x], gg) for x in range(i+1)]
            bb.sort()
            return bb[1]
        else:
            g = gcd(g, li[i])
    return g


def max_gcd(a):
    g = gcd_list(a)
    a = [a[i]//g for i in range(n)]
    m = gcd_list_2(a)
    print(g * m)


max_gcd(a)