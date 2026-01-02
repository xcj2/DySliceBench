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
     
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    g = gcd(a, b)
    return b * a // g

def main():
    N, M = LI()
    A = LI()
    g = 1
    for i in range(N):
        A[i] //= 2
        g = lcm(g, A[i])

    for a in A:
        if g // a % 2 == 1:
            continue
        else:
            print(0)
            return
    shou = M // g
    if shou % 2 == 1:
        shou -= 1
        ans = shou // 2
        ans += 1
    else:
        ans = shou // 2
    print(ans)


main()

