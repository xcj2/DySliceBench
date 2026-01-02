import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD


def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret

def geteach(n):
    ret = defaultdict(int)
    for i in range(2, n+1):
        while True:
            if n % i == 0:
                ret[i] += 1
                n //= i
            else:
                break

        if n == 1:
            break

    return ret


def getyaku(n):
    ret = defaultdict(int)

    for i in range(2, n+1):
        fac = geteach(i)
        for k, v in fac.items():
            ret[k] += v

    return ret

def solve():

    n = getN()
    yaku = (getyaku(n))
    # print(yaku)
    nanashi = 0
    yon = 0
    ni = 0
    nishi = 0
    ichisi = 0
    for v in yaku.values():
        if v >= 74:
            nanashi += 1
        if v >= 24:
            nishi += 1
        if v >= 14:
            ichisi += 1
        if v >= 4:
            yon += 1
        if v >= 2:
            ni += 1

    if yon < 2 or yon + ni < 3:
        print(0)
        return
    pat1 = nanashi
    pat2 = nishi * (ni - 1)
    pat3 = ichisi * (yon - 1)
    pat4 = yon * (yon-1) * (ni - 2) // 2

    print(max(pat1, 0) + max(pat2, 0) + max(pat3, 0) + max(pat4, 0))

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()