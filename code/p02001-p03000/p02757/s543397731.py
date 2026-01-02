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
def LSI(): return list(map(int, list(sys.stdin.readline().rstrip())))
def LSI2(N): return [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h): return [i for j in range(h)]
def FILL2(i,h,w): return [FILL(i,w) for j in range(h)]
def FILL3(i,h,w,d): return [FILL2(i,w,d) for j in range(h)]
def FILL4(i,h,w,d,d2): return [FILL3(i,w,d,d2) for j in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 998244353
INF = float("inf")
sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline

N,P = MI()
S = S()
mod = 0
ans = 0
dic = {0:1}
if P == 2 or P == 5:
    for i in range(N):
        if int(S[i])%P==0:
            ans += i+1
else:
    for i in range(N-1,-1,-1):
        mod = (mod+pow(10,(N-1-i),P)*int(S[i]))%P
        dic[mod] = dic.get(mod,0)+1
    for i in dic.values():
        ans += int(i*(i-1)/2)
print(ans)
