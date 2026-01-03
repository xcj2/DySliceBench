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
    N, M = LI()
    reachable_from_1 = set()
    reachable_to_N = []
    ships = []
    for _ in range(M):
        a, b = LI()
        ships.append((a, b))
        if b == N:
            reachable_to_N.append(a)
        if a == 1:
            reachable_from_1.add(b)
    ans = False
    for n in reachable_to_N:
        if n in reachable_from_1:
            ans = True
    if ans:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

main()

