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

N,L,T = MI()
for_l = []
rev_l = []
final = []
for i in range(N):
    if i==0:
        x0,w0 = MI()
        x,w = x0,w0
    else:
        x,w = MI()
    if w==1:
        for_l += [x]
        final += [(x+T)%L]
    else:
        rev_l += [x]
        final += [(x-T)%L]

final.sort()
opposite_l = rev_l if w0==1 else for_l
opp_num = len(opposite_l)
cicle = (2*T)//L
res = (2*T)%L
cnt = 0 #i=1のアリが衝突する回数
cnt += opp_num*cicle
if res!=0 and res!=1:
    xr = (x0 + res -1)%L if w0==1 else x0
    xl = x0 if w0==1 else (x0-res+1)%L
    for i in opposite_l:
        if xl<=xr and xl<=i<=xr:
            cnt += 1
        if xl>xr and (i>=xl or i<=xr):
            cnt += 1
c = (cnt)%N if w0==1 else (-cnt)%N #x0+Tにくるアリの番号
if w0==1:
    c_idx = final.index((x0+T)%L)
else:
    c_idx_l = [i for i,v in enumerate(final) if v==(x0-T)%L]
    c_idx = c_idx_l[-1]
ans = [-1 for i in range(N)]
ans[c] = final[c_idx]
for i in range(1,N):
    ans[(c+i)%N] = final[(c_idx+i)%N]
[print(x) for x in ans]
