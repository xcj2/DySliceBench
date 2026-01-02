import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h): return [i for j in range(h)]
def FILL2(i,h,w): return [FILL(i,w) for j in range(h)]
def FILL3(i,h,w,d): return [FILL2(i,w,d) for j in range(h)]
def FILL4(i,h,w,d,d2): return [FILL3(i,w,d,d2) for j in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**5+10)
input = sys.stdin.readline

K,N = MI()
l = LI()
max_dis = 0
for i in range(N):
    if i < N-1:
        next_dis = l[i+1]-l[i]
    else:
        next_dis = l[0]+(K-l[i])
    max_dis = max(max_dis,next_dis)
print(K-max_dis)
