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
    a = []
    for i in range(5):
        a.append(I())

    ans = inf
    for arr in itertools.permutations(range(5)):
        t = 0
        for j, i in enumerate(arr):
            t += a[i]
            if t % 10 != 0 and j < 4:
                t = (t // 10 + 1) * 10
        ans = min(ans, t)
    print(ans)

main()

