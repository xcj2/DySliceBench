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
    N, Q = LI()
    s = S()
    L, R = [], []
    for _ in range(Q):
        l, r = LI_()
        L.append(l)
        R.append(r)
    num_ac = [0] * len(s)
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i+1] == 'C':
            num_ac[i+1] += 1
    for i in range(1, len(s)):
        num_ac[i] += num_ac[i-1]
    for i in range(Q):
        print(num_ac[R[i]] - num_ac[L[i]])

main()

