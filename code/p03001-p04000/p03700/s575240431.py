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
    N, A, B = LI()
    H = []
    for _ in range(N):
        H.append(I())
    ng = -1
    ok = 10**9 + 1

    def enough(n, H):
        diff = A - B
        num = 0
        for i in range(N):
            H[i] -= B * n

        for i in range(N):
            if H[i] <= 0:
                continue
            num += H[i] // diff
            if H[i] % diff > 0:
                num += 1
        return num <= n

    while ok - ng > 1:
        attack = (ok + ng) // 2
        if enough(attack, H.copy()):
            ok = attack
        else:
            ng = attack

    print(ok)



main()

