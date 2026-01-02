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


n,m = LI()

ll = []
for i in range(m):
    ll.append(LI())

for i in range(0,1000):
    if len(str(i))!=n:
        continue
    s = str(i)
    flag = True
    for j in ll:
        if s[j[0]-1]!=str(j[1]):
            flag = False
            break
    if flag:
        print(i)
        exit()

print(-1)