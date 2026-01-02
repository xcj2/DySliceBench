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
    A = []
    for _ in range(N):
        a, b = LI()
        A.append((a, b))
    A = sorted(A, key=lambda x:x[0])
    bought = 0
    ix = 0
    money = 0
    while bought < M:
        if bought + A[ix][1] > M:
            money += A[ix][0] * (M - bought)
            break
        bought += A[ix][1]
        money += A[ix][0] * A[ix][1]
        ix += 1
    print(money)


main()

