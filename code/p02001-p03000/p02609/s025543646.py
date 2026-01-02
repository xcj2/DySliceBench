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


memo = {}

def countbit(x):
    i = 0
    cnt = 0
    while x >= 1<<i:
        if x & (1<<i):
            cnt += 1
        i += 1
    return cnt


def count(x):
    # if c == 0:
    #     return 0
    # s = 1
    # x = x % c
    s = 0
    while x != 0:
        s += 1
        x = x % countbit(x)
    return s

def main():
    n = int(input())
    xs = list(input())
    c = len([i for i in xs if i == '1'])
    dp = {}
    dps = {}
    for i in range(-1, 2):
        cc = c + i
        if cc == 0:
            continue
        dp[cc] = [-1] * n
        base = 1 % cc
        dpstmp = 0
        for i in range(n):
            dp[cc][i] = base
            if xs[-i-1] == '1':
                dpstmp += base
            base = base * 2 % cc
        dps[cc] = dpstmp % cc

    for i in range(n):
        cc = c
        if xs[i] == '1':
            cc -= 1
        else:
            cc += 1
        if cc == 0:
            print(0)
            continue
        res = dps[cc]
        if xs[i] == '1':
            res = (res - dp[cc][-i-1]) % cc
        else:
            res = (res + dp[cc][-i-1]) % cc
        s = count(res) + 1
        print(s)


main()
