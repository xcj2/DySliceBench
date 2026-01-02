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

g_cnt = 0
def main():
    N = I()
    dp = [[[[0 for _ in range(4)] for ____ in range(4)] for __ in range(4)] for ___ in range(N+1)]
    s2i = {
        'A': 0,
        'G': 1,
        'C': 2,
        'T': 3,
    }
    dp[0][3][3][3] = 1

    for i in range(0, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for char in ['A', 'G', 'C', 'T']:
                        if char == 'G':
                            if k == s2i['A'] and l == s2i['C']:
                                continue
                        elif char == 'C':
                            if j == s2i['A'] and l == s2i['G']:
                                continue
                            if k == s2i['G'] and l == s2i['A']:
                                continue
                            if k == s2i['A'] and l == s2i['G']:
                                continue
                            if j == s2i['A'] and k == s2i['G']:
                                continue
                        else:
                            pass
                        dp[i+1][k][l][s2i[char]] += dp[i][j][k][l]
                        dp[i+1][k][l][s2i[char]] %= mod

    cnt = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                cnt += (dp[N][j][k][l] % mod)
                cnt %= mod
    print(cnt)
main()

