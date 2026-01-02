import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

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


def solve():
    n = getN()
    S = getS()
    l = 0
    r = n - 1
    # print(n, S, l, r)
    ansl, ansr = 0,0
    while S[r] == "W":
        r -= 1
        if l == r:
            print(max(ansl, ansr))
            return
    while True:
        while True:
            if S[l] == "W":
                l += 1
                ansl += 1
                # print(ansl, l, r)
                while S[l] == "R":
                    if l == r:
                        print(max(ansl, ansr))
                        return
                    l += 1
                break
            l += 1
            if l == r:
                break
            # print(l, r?)
        if l == r:
            print(max(ansl, ansr))
            return

        while True:
            if S[r] == "R":
                r -= 1
                ansr += 1
                while S[r] == "W":
                    if l == r:
                        print(max(ansl, ansr))
                        return
                    r -= 1
                break
            r -= 1
            if r == l:
                break
            # print(l, r)
        if l == r:
            print(max(ansl, ansr))
            return
    # ans2 = rc - rcnt
    # print(min(ans1,ans2))


def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()