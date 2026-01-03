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
    n, m = LI()
    x = sorted(LI())
    y = sorted(LI())
    ans = 0
    for i in range(len(x)):
        k = i + 1
        ans += (k - 1 - n + k) * x[i]
    ysum = 0
    for j in range(len(y)):
        k = j + 1
        ysum += (k - 1 - m + k) * y[j]
    ans *= ysum
    ans %= mod
    print(ans)

main()

