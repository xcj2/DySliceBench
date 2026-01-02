#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    lis = []
    c = []
    rev = []
    for _ in range(n):
        a,b = input().split()
        b = int(b)
        a = list(a)
        lis.append(a)
        rev.append(a[::-1])
        c.append(b)
    res = defaultdict(lambda : float("inf"))
    q = [(0,[],[])]
    res[(tuple(),tuple())] = 0
    while q:
        d,pre,suf = heappop(q)
        ns = pre+suf[::-1]
        if ns != [] and ns == ns[::-1]:
            print(d)
            return
        if len(pre) <= len(suf):
            k = suf[len(pre):]
            for i in range(n):
                s = lis[i]
                m = min(len(s),len(k))
                if k[:m] == s[:m]:
                    npre = pre+s
                    re = d+c[i]
                    i = tuple(npre)
                    j = tuple(suf)
                    if re < res[(i,j)]:
                        res[(i,j)] = re
                        heappush(q,(re,npre,suf))
        else:
            k = pre[len(suf):]
            for i in range(n):
                s = rev[i]
                m = min(len(s),len(k))
                if k[:m] == s[:m]:
                    nsuf = suf+s
                    re = d+c[i]
                    i = tuple(pre)
                    j = tuple(nsuf)
                    if re < res[(i,j)]:
                        res[(i,j)] = re
                        heappush(q,(re,pre,nsuf))
    print(-1)
    return

#Solve
if __name__ == "__main__":
    solve()
