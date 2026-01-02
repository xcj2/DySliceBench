import sys
import math
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
sys.setrecursionlimit(10**5+10)
input = sys.stdin.readline

N = I()
prev_t = 0
prev_x = 0
prev_y = 0
flag = True
for i in range(N):
    t,x,y = map(int,input().split())
    t = t-prev_t
    if abs(x-prev_x)+abs(y-prev_y) > t:
        flag = False
        break
    elif (abs(x-prev_x)+abs(y-prev_y)) %2 != t%2:
        flag = False
        break
    prev_t = t+prev_t
    prev_x = x
    prev_y = y
print('Yes' if flag else 'No')
