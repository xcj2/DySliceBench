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
def input(): return sys.stdin.readline().rstrip()
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

def cnt_two(n):
  if n % 2 == 1:
    return 0
  else:
    return 1 + cnt_two(n // 2)

N = iIn()
A = iInLH()

ans = INF
for i in range(N):
  cnt = cnt_two(A[i])
  ans = min(ans, cnt)
  
print(ans)