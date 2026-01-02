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
import pdb
     
def main():
    N = S()
    K = I()
    dp = [[[0 for _ in range(102)] for __ in range(2)] for ___ in range(102)]
    dp[0][0][0] = 1
    for i in range(1, len(N)+1):
        for j in range(2):
            if j == 1:
                max_dig = 9
            else:
                max_dig = int(N[i-1])
            for k in range(i+1):
                for d in range(max_dig + 1):
                    if d < max_dig:
                        # kakutei
                        miman = 1
                    else:
                        miman = 0
                        if j == 1:
                            miman = 1
                    if d != 0:
                        newK = k + 1
                    else:
                        newK = k
                    dp[i][miman][newK] += dp[i-1][j][k]

    print(dp[len(N)][0][K] + dp[len(N)][1][K])
main()

