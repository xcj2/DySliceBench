import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
from bisect import bisect_left
from itertools import product
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
#文字列を一文字ずつ数字に変換、'5678'を[5,6,7,8]とできる
def LSI(): return list(map(int, list(sys.stdin.readline().rstrip())))
def LSI2(N): return [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
#文字列として取得
def ST(): return sys.stdin.readline().rstrip()
def LST(): return sys.stdin.readline().rstrip().split()
def LST2(N): return [sys.stdin.readline().rstrip().split() for i in range(N)]
def FILL(i,h): return [i for j in range(h)]
def FILL2(i,h,w): return [FILL(i,w) for j in range(h)]
def FILL3(i,h,w,d): return [FILL2(i,w,d) for j in range(h)]
def FILL4(i,h,w,d,d2): return [FILL3(i,w,d,d2) for j in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**6+10)

N  = I()
A = LI()
sum = [0]*(N+2)
sum[N] = A[N]
for i in range(N-1,-1,-1):
    sum[i] = sum[i+1]+A[i]

if N==0:
    if A[0]==1:
        print(1)
    else:
        print(-1)
else:
    if A[0]!=0:
        print(-1)
    else:
        ans = 1
        b = 1
        for i in range(1,N+1):
            a = A[i]
            b_ = sum[i+1]
            if b_<b-a or 2*b-a<0:
                print(-1)
                break
            b_ = min(b_, 2*b-a)
            ans += a+b_
            b = b_
        else:
            print(ans)
