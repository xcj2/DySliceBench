import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def judge(g):
    n = len(g)
    bi = [-1] * n
    bi[0] = 0
    for cn in range(n):
        for i, row in enumerate(g):
            for j, column in enumerate(row):
                if column == "1":
                    if bi[i] == -1 and bi[j] == -1:
                        pass
                    elif bi[i] == -1:
                        bi[i] = bi[j] ^ 1
                    elif bi[j] == -1:
                        bi[j] = bi[i] ^ 1
                    else:
                        if bi[i] == bi[j]:
                            print(-1)
                            sys.exit()




def solve():
    n = getN()
    g = []
    for i in range(n):
        g.append([c for c in getS()])

    judge(g)

    costs = [[INF for i in range(n)] for j in range(n)]
    for i in range(n):
        costs[i][i] = 0

    for i, row in enumerate(g):
        for j, column in enumerate(row):
            if column == "1":
                costs[i][j] = 1

    V = n
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if costs[i][k] != INF and costs[k][j] != INF:
                    costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    ans = max([max(x) for x in costs])
    print(ans + 1)

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()