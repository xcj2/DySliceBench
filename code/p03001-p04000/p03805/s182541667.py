###==================================================
### import
#import bisect
from collections import Counter, deque, defaultdict
from copy import deepcopy
#from functools import reduce, lru_cache
#from heapq import heappush, heappop
#import itertools
#import math
#import string
import sys
### stdin
def input(): return sys.stdin.readline()
def iIn(): return int(input())
def iInM(): return map(int, input().split())
def iInM1(): return map(int1, input().split())
def iInLH(): return list(map(int, input().split()))
def iInLH1(): return list(map(int1, input().split()))
def iInLV(n): return [iIn() for _ in range(n)]
def iInLV1(n): return [iIn()-1 for _ in range(n)]
def iInLD(n): return [iInLH() for _ in range(n)]
def iInLD1(n): return [iInLH1() for _ in range(n)]
def sInLH(): return list(input().split())
def sInLV(n): return [input().rstrip('\n') for _ in range(n)]
def sInLD(n): return [sInLH() for _ in range(n)]
### stdout
def OutH(lst, deli=' '): print(deli.join(map(str, lst)))
def OutV(lst): print('\n'.join(map(str, lst)))
### setting
sys.setrecursionlimit(10 ** 6)
### utils
int1 = lambda x: int(x) - 1
### constants
INF = int(1e9)
MOD = 1000000007
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
###---------------------------------------------------

N, M = iInM()
AB = iInLD(M)

ans = 0
q= deque([[[1], []]]) # [[nodes], [edges]]

while len(q) > 0:
    n, e = q.pop()
    if len(n) == N:
        ans += 1
        continue
    for i in range(M):
        if i in e:
            continue
        if AB[i][0] == n[-1]:
            if AB[i][1] not in n:
                new_n = n[:]
                new_e = e[:]
                new_n.append(AB[i][1])
                new_e.append(i)
                q.append([new_n, new_e])
                continue
        if AB[i][1] == n[-1]:
            if AB[i][0] not in n:
                new_n = n[:]
                new_e = e[:]
                new_n.append(AB[i][0])
                new_e.append(i)
                q.append([new_n, new_e])
                continue

print(ans)
        