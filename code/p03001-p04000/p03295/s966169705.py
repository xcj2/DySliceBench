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

def era(n):
    ret = [1 for i in range(n + 2)]
    for i in range(2, int(math.sqrt(n) +3)):
        if ret[i] != 0:
            for j in range(2, n//i + 1):
                ret[i * j] = 0
    rret = []
    for i, r in enumerate(ret):
        if r == 1 and i != 0:
            rret.append(i)

    return rret


def houjyo(n, m, k, kaijyo):
    # kaburi ... k
    # all ... n
    if k == n:
        return 1
    else:
        # kasanarierabi nck * nokorierabi (m - k)p(n-k) - houjyo(+1)
        ret = nck(n,k,kaijyo) * npk(m-k, n-k, kaijyo) # - (k + 1) * houjyo(n, m, k+1, kaijyo)
        # print(nck(n,k,kaijyo) , npk(m-k, n-k, kaijyo))
        return ret % MOD


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
    n, m = getList()
    kukan = []
    for i in range(m):
        a, b = getList()
        kukan.append((a, b))

    kukan.sort(key=lambda x: x[1])
    # for ku in kukan:
    #     print(ku)
    kiru = 0
    ans = 0
    for ku in kukan:
        a, b = ku
        if a >= kiru:
            ans += 1
            kiru = b

    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()