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
    a = IR(5)
    k = II()
    if max(a) - min(a) > k:
        print(":(")
    else:
        print("Yay!")
    return

#B
def B():
    a = IR(5)
    b = a[0]
    ans = 0
    for a_ in a:
        if a_ % 10 != 0:
            if b % 10> a_ % 10:
                b = a_
    flg = 0
    for a_ in a:
        if a_ != b or flg:
            ans += math.ceil(a_ / 10) * 10
        else:
            ans += b
            flg = 1
    print(ans)
            
    
    return

#C
def C():
    n = II()
    ai = IR(5)
    print(math.ceil(n / min(ai)) + 4)
        
        
    return

#D
def D():
    x, y, z, K = LI()
    a = LI()
    a.sort(reverse=True)
    b = LI()
    b.sort(reverse = True)
    c = LI()
    c.sort(reverse=True)
    ab = []
    for a_ in a:
        for b_ in b:
            ab.append(a_ + b_)
    ab.sort(reverse = True)
    ab = ab[:K]
    ans = []
    for ab_ in ab:
        for c_ in c:
            ans.append(ab_ + c_)
    ans.sort(reverse = True)
    for k in range(K):
        print(ans[k])



        
                    

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
    D()