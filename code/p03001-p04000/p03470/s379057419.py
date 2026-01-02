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

#A
def A():
    s = S()
    s[3] = "8"
    print("".join(s))
    return

#B
def B():
    n = II()
    d = IR(n)
    d.sort(reverse=True)
    b = float("inf")
    ans = 0
    for i in d:
        if i < b:
            ans += 1
            b = i
    print(ans)
    return

#C
def C():
    return

#D
def D():
    n, h = LI()
    ab = LIR(n)
    ab.sort(reverse=True)
    amax = ab[0][0]
    ab.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    hp = 0
    for a,b in ab:
        if b <= amax:
            break
        ans += 1
        hp += b
        if hp >= h:
            break
    ans += max(math.ceil((h-hp)/amax),0)    
    print(ans)
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
    B()
