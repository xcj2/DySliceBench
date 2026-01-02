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
    H = LI()
    H = [0] + H + [10**9+1]
    for i in range(1, N+1):
        l = H[i-1]
        m = H[i]
        r = H[i+1]
        if m > r:
            if l == m:
                print("No")
                return
            elif l < m:
                if not H[i] - 1 == r:
                    print("No")
                    return
            else:
                print("No")
                return
        else:
            pass
        if l != m:
            H[i] -= 1
    print("Yes")

main()

