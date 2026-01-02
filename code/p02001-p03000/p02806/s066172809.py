import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys

sys.setrecursionlimit(10**9)
mod = 998244353
inf = 10**20

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

n = I()
s = []
t = []
for i in range(n):
    S,T = LS()
    s.append(S)
    t.append(int(T))
x = input()

idx = s.index(x)
if idx==n-1:
    print(0)
    exit()
print(sum(t[idx+1:]))
