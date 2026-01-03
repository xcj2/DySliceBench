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

def factor(n):
    rt_n = int(math.sqrt(n)) + 2
    for i in range(1, rt_n):
        if n % i == 0:
            yield (i, n//i)

def main():
    N = I()
    ans = inf
    for s1, s2 in factor(N):
        f = max(len(str(s1)), len(str(s2)))
        ans = min(ans, f)
    print(ans)



main()

