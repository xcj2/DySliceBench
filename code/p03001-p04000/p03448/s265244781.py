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

def solve():
    a =getN()
    b=getN()
    c=getN()
    x=getN()
    ans = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if 500 * i + 100 * j + 50 * k == x:
                    ans += 1


    print(ans)


def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()