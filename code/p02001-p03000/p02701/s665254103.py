import sys
import math
from collections import deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def S(): return sys.stdin.readline()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h,w): return [[i for j in range(w)] for k in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**6+10)


N = I()
l = [input() for i in range(N)]
d = {}
ans = 0
for item in l:
    if item in d:
        continue
    else:
        ans += 1
        d[item] = 1
        continue
print(ans)
