import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

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


def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret

def judge(anums, k, mid):
    if mid == 0:
        return False
    tmp = 0
    for anum in anums:
        tt = anum // mid
        if mid * tt != anum:
            tt += 1
        tmp += tt - 1

    if tmp <= k:
        return True
    else:
        return False

def solve():
    n, k = getList()
    anums = getList()

    mn = 0
    mx = sum(anums) + 1
    while(mx - mn > 1):
        mid = (mn + mx) // 2
        if judge(anums, k, mid):
            mx = mid
        else:
            mn = mid

    if judge(anums, k, mn):
        print(mn)
    else:
        print(mx)


def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()