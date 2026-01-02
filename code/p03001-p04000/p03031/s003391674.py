#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, p = LI()
    print((a*3+p)//2)
    return

#B
def B():
    n = II()
    sp = []
    for i in range(n):
        sp.append(input().split())
    another = [(s[0], -1 * int(s[1]),num) for num,s in enumerate(sp)]
    another.sort()
    for s,p,q in another:
        print(q+1)

    return

#C
def C():
    n, m = LI()
    ks = LIR_(m)
    p = LI()
    patern = itertools.product(range(2), repeat=n)
    ans = 0
    for on in patern:
        ki = [0 for i in range(m)]
        for num, oni in enumerate(on):
            if oni:
                for i,ksi in enumerate(ks):
                    ksi = ksi[1::]
                    if num in ksi:
                        ki[i] ^= 1
        #print(ki)
        for num, pi in enumerate(p):
            if pi != ki[num]:
                break
        else:
            ans += 1
    print(ans)

            
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    C()
