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
    bars = []
    for _ in range(M):
        a, b = LI_()
        bars.append((a,b))
    bars = sorted(bars, key=lambda x: x[0])
    l_max = bars[0][0]
    r_min = bars[0][1]

    count = 1 
    for bar in bars[1:]:
        l, r = bar
        if r_min <= l:
            count += 1
            r_min = r
        else:
            r_min = min(r, r_min)
        l_max = l

    print(count)
main()

