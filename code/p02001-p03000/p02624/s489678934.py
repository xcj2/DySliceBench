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


def solve():
    n = getN()
    # sosu = era(n)

    ans = 0
    for so in range(1, n+1):
        kazu = n // so
        ans += so * (kazu * (kazu+1) // 2)
        # print(so, ans)


    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()