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
    N, K = LI()
    baisu = set()
    khalf = set()
    cnt = 0
    gusu = (K % 2 == 0)
    for x in range(1, N+1):
        if gusu and x % K == K // 2:
            khalf.add(x)
            continue
        if x % K != 0:
            continue
        baisu.add(x)
    cnt += len(baisu) ** 3
    cnt += len(khalf) ** 3
    print(cnt)


main()

