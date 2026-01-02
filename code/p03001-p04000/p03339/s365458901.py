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
    s = S()
    west = [0] * (N+1)
    east = [0] * (N+1)

    for i, c in enumerate(s):
        if c == 'W':
            west[i] = 1
        else:
            east[i] = 1

    for i in range(N):
        west[i+1] += west[i]

    for i in range(N)[::-1]:
        east[i] += east[i+1]

    min_c = inf
    ans_i = -1
    for i in range(N):
        if i == 0:
            tot = east[i+1]
        elif i == N-1:
            tot = west[i-1]
        else:
            tot = west[i-1] + east[i+1]

        min_c = min(min_c, tot)
    print(min_c)
main()

