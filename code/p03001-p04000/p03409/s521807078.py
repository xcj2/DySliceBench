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
    return

#B
def B():
    return

#C
def C():
    n = II()
    ab = LIR(n)
    cd = LIR(n)
    ab.sort()
    cd.sort()
    check = [0 for i in range(n)]
    ans = 0
    #print(ab)
    for i, c in enumerate(cd):
        d = c[1]
        c = c[0]
        maxy = -1
        x = -1
        for k, a in enumerate(ab):
            b = a[1]
            a = a[0]
            if maxy < b and c > a and check[k] == 0 and d > b:
                maxy = b
                x = k
                #print(a,b,c,d)
        if x != -1:
            ans += 1
            check[x] += 1
    print(ans)


    return

#D
def D():
    n = II()
    ab = LI()
    cd = LI()
    binab = []
    bincd = []
    warerua = [0 for i in range(28)]
    wareruc = [0 for i in range(28)]
    warenaib = [0 for i in range(28)]
    warenaid = [0 for i in range(28)]
    for i in range(n):
        ab[i] = list(bin(ab[i]))[2:]
        ab[i] = ab[i][::-1]
        cd[i] = list(bin(cd[i]))[2:]
        cd[i] = cd[i][::-1]
    for i in range(n):
        for k in range(len(ab[i])):
            #print(warerua, warenaib, wareruc, warenaid,ab[i][k])
            if ab[i][k] == "1":
                warenaib[k] += 1
            else:
                warerua[k] += 1
        for k in range(len(ab[i]), 28):
            warerua[k] += 1
        for k in range(len(cd[i])):
            if cd[i][k] == "1":
                warenaid[k] += 1
            else:
                wareruc[k] += 1
        for k in range(len(ab[i]), 28):
            wareruc[k] += 1
    ans = 0
    print(warerua, warenaib, wareruc, warenaid)
    for i in range(28):
        kisu = warerua[i] * warenaid[i] + warenaib[i] * wareruc[i]
        gusu = warerua[i] * wareruc[i] + warenaib[i] * warenaid[i]
        if kisu % 2:
            ans += 1 << i
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
    C()
