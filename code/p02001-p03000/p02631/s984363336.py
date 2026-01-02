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
#OutH = print(' '.join(map(str, lst)))
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

## 数値リストを与えるとそのxorを計算する
## xors([1,2,3]) = 0
def xors(num_lst):
  xor = 0
  for i in range(len(num_lst)):
    xor = xor ^ num_lst[i]
  return xor

N = iIn()
A = iInLH()

allxor = xors(A)
lst = []
for i in range(N):
    eachxor = allxor ^ A[i]
    lst.append(eachxor)

print(' '.join(map(str, lst)))
