import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import copy

sys.setrecursionlimit(10**9)
mod = 10**7+9
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
di = collections.defaultdict(int)

for i in range(n):
    s = S()
    di[s]+=1

mx = 0
l = []
for i in di:
    if mx<di[i]:
        l = [i]
        mx = di[i]
    elif mx==di[i]:
        l.append(i)
l.sort()
for v in l:
    print(v)