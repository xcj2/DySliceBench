import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, T = LI()
    AB = []
    for i in range(N):
        _a, _b = LI()
        AB.append((_a, _b))
    AB = sorted(AB, key=lambda x: (x[0], x[1]))
    a = [elem[0] for elem in AB]
    b = [elem[1] for elem in AB]

    dp = [[0 for _ in range(T + 3001)] for _ in range(N+1)]
    for i in range(N):
        for t in range(T):
            dp[i+1][t+a[i]] = max(dp[i+1][t+a[i]], dp[i][t] + b[i])
            dp[i+1][t] = max(dp[i+1][t], dp[i][t])
    ans = 0
    for i in range(N+1):
        for j in range(T + 3001):
            ans = max(dp[i][j], ans)
    print(ans)
main()

