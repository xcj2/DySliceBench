from heapq import heappush, heappop
from collections import deque
import re
import math
import functools
import itertools
import fractions

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))


INF = 1 << 29


def mk1d(n, val=INF):
    return [val for i in range(n)]

def mk2d(h, w, val=INF):
    return [[val for i in range(w)]for i in range(h)]

DIV = 998244353

def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return functools.reduce(lcm_base, numbers, 1)


def floyd_warshall(costs):
    N = len(costs)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                costs[i][j] = min(costs[i][j], costs[i][k]+costs[k][j])
    return costs

def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)

def main():
    H,W = isRaw()
    SS = [sRaw() for _ in range(H)]
    costs = mk2d(H*W, H*W, INF)
    for h in range(H):
        for w in range(W):
            cur = h*W+w
            costs[cur][cur] = 0
            if h<H-1 and SS[h][w]=="." and SS[h+1][w]==".":
                costs[cur][cur+W] = 1
                costs[cur+W][cur] = 1
            if w < W-1 and SS[h][w] == "." and SS[h][w+1] == ".":
                costs[cur][cur+1] = 1
                costs[cur+1][cur] = 1                
    costs = floyd_warshall(costs)
    maxCost = 0
    for cur in range(H*W):
        for nxt in range(H*W):
            if(costs[cur][nxt]!=INF) and cur!=nxt:
                maxCost = max(maxCost,costs[cur][nxt])
    return maxCost

if __name__ == "__main__":
    print(main())
