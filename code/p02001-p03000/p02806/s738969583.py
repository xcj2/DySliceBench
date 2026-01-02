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
    s, t = [], []
    for _ in range(N):
        _s, _t = LS()
        _t = int(_t)
        s.append(_s)
        t.append(_t)
    X = S()
    for i, title in enumerate(s):
        if title == X:
            break
    i += 1
    cnt = 0
    for j in range(i, N):
        cnt += t[j]
    print(cnt)
main()

