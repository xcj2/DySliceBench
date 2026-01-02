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

def isOk(n):
    a = 0
    for i in range(1, n+1):
        if n % i == 0:
            a += 1
    return a == 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            continue
        if isOk(i):
            ans += 1

    print(ans)



main()
