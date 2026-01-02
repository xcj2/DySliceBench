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
    N = I()
    G = []
    for _ in range(N):
        a = LI()
        G.append(a)
    dp = copy.deepcopy(G)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
 
    if dp != G:
        print(-1)
        return
 
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if j == k:
                    continue
                if i == k:
                    continue
                if dp[i][k] == 0 or dp[i][j] == 0 or dp[j][k] == 0:
                    continue
                if dp[i][j] == dp[i][k] + dp[k][j]:
                    dp[i][j] = 0
                    dp[j][i] = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += dp[i][j]
    print(cnt // 2)
main()
