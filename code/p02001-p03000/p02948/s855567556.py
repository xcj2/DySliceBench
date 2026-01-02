from heapq import heappush, heappop
import re
from collections import deque
import sys
import math
input = sys.stdin.readline


def int_raw():
    return int(input())


def ss_raw():
    return input().split()


def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


def ncr(n, r, mod=DIV):
	r = min(r, n-r)
	ret = 1
	for i in range(1, r+1):
		ret = ret * (n-i+1) % mod
		ret = ret * mod_inv(i, mod) % mod
	return ret


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.mini = [i for i in range(n+1)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        mini = min(self.mini[x],self.mini[y])
        self.mini[x]=mini
        self.mini[y]=mini
    
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

def main():
    N ,M = ints_raw()
    days = [0]*M
    uft = UnionFind(M)
    ABs = [ints_raw() for _ in range(N)]
    ABs.sort(key=lambda x:x[1],reverse=True)
    ans = 0
    for AB in ABs:
        A,B = AB
        if A > M:
            continue
        else:
            C = M-A
            par = uft.mini[uft.find(C)]

            if days[par] == 0:
                days[par]=1
                ans += B
                #uft.union(par,C)
                if par > 0:
                    uft.union(par-1,par)

            #while days[C]==1 and C>=0:
            #    C-=1
            #if C>=0:
            #    days[C]=1
            #    ans+=B
    return ans

    
print(main())
