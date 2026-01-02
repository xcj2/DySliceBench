import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
import heapq

sys.setrecursionlimit(1000000)

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


def fact_and_inv(SIZE):
    inv = [0] * SIZE  # inv[j] = j^{-1} mod MOD
    fac = [0] * SIZE  # fac[j] = j! mod MOD
    finv = [0] * SIZE  # finv[j] = (j!)^{-1} mod MOD
    inv[1] = 1
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, SIZE):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return fac, finv

def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret


def solve():
    x, y, a, b, c = getList()
    anums = getList()
    bnums = getList()
    cnums = getList()
    q = []
    anums.sort(key=lambda x: -x)
    bnums.sort(key=lambda x: -x)
    cnums.sort(key=lambda x: -x)
    for i, num in enumerate(anums):
        if i == x:
            break
        heapq.heappush(q, -num)
    for i, num in enumerate(bnums):
        if i == y:
            break
        heapq.heappush(q, -num)

    for i, num in enumerate(cnums):
        # if i == b:
        #     break
        heapq.heappush(q, -num)

    ans = 0
    for i in range(x + y):
        ans += heapq.heappop(q)

    print(-ans)

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()