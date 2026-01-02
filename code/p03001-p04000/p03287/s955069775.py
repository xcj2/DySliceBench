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
     
def nc2(n):
    return n * (n-1) // 2
def main():
    n, m = LI()
    A = LI()
    cnt = 0
    cumsum = [0] * (n+1)
    d = collections.defaultdict(int)
    for i in range(n):
        cumsum[i+1] = (cumsum[i] % m + A[i] % m) % m
        d[cumsum[i+1]] += 1
    for k, v in d.items():
        cnt += nc2(v)
        if k % m == 0:
            cnt += v
    print(cnt)



main()

