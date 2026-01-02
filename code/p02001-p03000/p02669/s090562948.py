import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

dic = dict()

def search(n, a, b, c, d):
    # print(n, dic)
    if n == 0:
        return 0
    if n == 1:
        return d
    if n in dic:
        return dic[n]

    ret = n * d

    tgt = n // 2
    ret = min(ret, search(tgt, a, b, c, d) + a + d * abs(tgt * 2 - n))
    tgt = (n + 1) // 2
    ret = min(ret, search(tgt, a, b, c, d) + a + d * abs(tgt * 2 - n))

    tgt = n // 3
    ret = min(ret, search(tgt, a, b, c, d) + b + d * abs(tgt * 3 - n))
    tgt = (n + 2) // 3
    ret = min(ret, search(tgt, a, b, c, d) + b + d * abs(tgt * 3- n))

    tgt = n // 5
    ret = min(ret, search(tgt, a, b, c, d) + c + d * abs(tgt * 5 - n))
    tgt = (n + 4) // 5
    ret = min(ret, search(tgt, a, b, c, d) + c + d * abs(tgt * 5 - n))

    dic[n] = ret
    return ret

def solve():
    N, A, B, C, D = getList()
    dic.clear()
    print(search(N, A, B, C, D))

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    main()
    # solve()





