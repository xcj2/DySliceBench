###==================================================
### import
#import bisect
#from collections import Counter, deque, defaultdict
#from copy import deepcopy
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
def OutH(lst, delimiter=' '): print(delimiter.join(map(str, lst)))
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

N_AROUND = 8
ddx = (-1, 0, 1, -1, 1, -1, 0, 1)
ddy = (-1, -1, -1, 0, 0, 1, 1, 1)

H, W = iInM()
S = sInLV(H)

## 周りに空きマスを入れる
T = [['.'] * (W + 2)]
for i in range(H):
    var = ['.'] + list(S[i]) + ['.']
    T.append(var)
T.append(['.'] * (W + 2))
#OutV(T)

ans = []
for i in range(1, H+1):
    ans.append([])
    for j in range(1, W+1):
        if T[i][j] == '#':
            ans[-1].append('#')
            continue
        cnt = 0
        for k in range(N_AROUND):
            if T[i + ddy[k]][j + ddx[k]] == '#':
                cnt += 1
        ans[-1].append(str(cnt))
        #print(ans)
#OutV(ans)

for i in range(H):
    OutH(ans[i], delimiter='')
