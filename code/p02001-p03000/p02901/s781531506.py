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
    N, M = LI()
    A = []
    C = []
    for i in range(M):
        a, _ = LI()
        bit = 0
        A.append(a)
        c = LI()
        for ix in c:
            bit = bit | 1 << (ix-1)
        C.append(bit)
    dp = [[inf for _ in range(1 << N)] for __ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(1 << N):
            # use i-th key
            dp[i+1][j | C[i]] = min(dp[i+1][j | C[i]], dp[i][j] + A[i])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    ans = dp[M][(1 << N) - 1]
    if ans == inf:
        print(-1)
        return
    print(ans)
    return

main()

