import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def SI(): return input().split()

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import ceil, floor, log2
from collections import deque
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product

def solve():
    n = II()

    V = [[] for _ in range(n)]
    for i in range(n):
        a, b, c = MI()
        V[i] = [a, b, c]

    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        dp[0][i] = V[0][i]

    # dp[i][0] -> dp[i+1][1], dp[i+1][2]
    for i in range(1, n):

        for j in range(3):
            for k in range(3):
                if j == k: continue
                dp[i][k] = max(dp[i-1][j] + V[i][k], dp[i][k])
    print(max(dp[-1]))


if __name__ == '__main__':
    solve()
