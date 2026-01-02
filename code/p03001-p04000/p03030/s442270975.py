import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return int(input())
from collections import defaultdict
from operator import itemgetter

n = SI()
dicts = []
for i in range(n):
    s, p = LS()
    p = int(p)
    dicts.append((i+1, s, p))
dicts = sorted(dicts, key=lambda x:(x[1],-x[2]))
for i, s, p in dicts:
    print(i)