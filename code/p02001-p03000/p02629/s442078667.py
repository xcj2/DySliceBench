###==================================================
### import
#import bisect
#from collections import Counter, deque, defaultdict
#from copy import deepcopy
#from functools import reduce, lru_cache
#from heapq import heappush, heappop
#import itertools
#import math
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
OutV = lambda x: print(*x, sep='\n')
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

## 10進数をn進数に変換(出力はstr)
## in: int X
## in: int n
## out: str
## (n-1)の桁数に合わせて0埋めをする
def Base_10_to_n(X, n):
    digit = len(str(n - 1))
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n).zfill(digit)
    return str(X%n).zfill(digit)

import string
alphabet = list(string.ascii_lowercase)


N = iIn()

s = Base_10_to_n(N, 26)

lst = []
for i in range(len(s)//2):
    var = s[2*i] + s[2*i+1]
    lst.append(int(var))
lst = lst[::-1]
## N = 26 -> lst = [0, 1]

solver = []
for i in range(len(lst)):
    if lst[i] > 0:
        solver.append(lst[i])
    else:
        if i == len(lst) - 1:
            break
        lst[i+1] -= 1
        solver.append(lst[i]+26)
solver = solver[::-1]

ans = ''
for i in range(len(solver)):
    ans += alphabet[solver[i]-1]

print(ans)