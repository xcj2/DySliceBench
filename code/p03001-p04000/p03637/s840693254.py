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
    A = LI()
    twos = []
    for a in A:
        if a % 4 == 0:
            cnt = 2
        elif a % 2 == 0:
            cnt = 1
        else:
            cnt = 0
        twos.append(cnt)
    if N % 2 == 0:
        minNeed = N
    else:
        minNeed = N - 2
    if sum(twos) < minNeed:
        print('No')
    else:
        print('Yes')
main()

