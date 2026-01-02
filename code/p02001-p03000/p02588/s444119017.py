import sys
import math
import copy
import random
import itertools
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

def getnigo(num):
    org = num
    if num in dic:
        return dic[num]
    ni, go = 0, 0
    while num % 2 == 0:
        ni += 1
        num //= 2
    while num % 5 == 0:
        go += 1
        num //= 5

    ni, go = min(18, ni), min(18, go)
    dic[org] = (ni, go)
    return ni, go

def solve(n=None, s1=None, s2=None):
    n = getN()
    li = []
    for i in range(n):
        s = getS()
        if "." not in s:
            num = int(s) *  10 ** 9
        else:
            sei, syo = s.split(".")
            num = int(sei) * 10 ** 9 + int(syo) * 10 ** (9 - len(syo))
        li.append(num)

    nigoli = [[0 for i in range(20)] for i in range(20)]

    for num in li:
        ni, go = getnigo(num)
        nigoli[ni][go] += 1

    for i in range(20):
        for j in range(18, -1, -1):
            nigoli[i][j] += nigoli[i][j+1]

    for i in range(18, -1, -1):
        for j in range(20):
            nigoli[i][j] += nigoli[i+1][j]

    # for lili in nigoli:
    #     print(lili)

    ans = 0
    for num in li:
        ni, go = getnigo(num)
        tni, tgo = 18 - ni, 18 - go
        ans += nigoli[tni][tgo]
        if ni >= 9 and go >= 9:
            ans -= 1
        # print(num, ni, go, ans)

    print(ans // 2)
    # print(getnigo(1))




def main():
    for _ in range(n):
        solve()
    return


if __name__ == "__main__":
    # main()
    solve()
