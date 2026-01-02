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
    A = LI()
    num2match = {
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
    }
    dp = ['' for _ in range(N+1)]
    for a in A:
        match_need = num2match[a]
        if 0 <= match_need <= N:
            dp[match_need] = max(str(dp[match_need]), str(a))
    for i in range(N+1):
        for a in A:
            match_need = num2match[a]
            if i - match_need > 0:
                if dp[i-match_need] == '':
                    continue
                old = dp[i]
                new = str(a) + dp[i-match_need]
                if len(old) > len(new):
                    dp[i] = old
                elif len(new) > len(old):
                    dp[i] = new
                else:
                    dp[i] = max(old, new)
    print(dp[N])
main()

