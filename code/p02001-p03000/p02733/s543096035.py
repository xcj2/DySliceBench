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
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline


ans = INF
H,W,K = MI()
s = LSI2(H)
for pattern in product([0,1],repeat=H-1):
    cut = 0
    before_idx = 0
    row_list = []
    for i,div in enumerate(pattern):
        if div==1:
            cut += 1
            square = s[before_idx:i+1]
            inv = list(zip(*square))
            row = [sum(inv[i]) for i in range(W)]
            row_list.append(row)
            before_idx = i+1
    square = s[before_idx:] #のこりのブロック
    inv = list(zip(*square))
    row_list.append([sum(inv[i]) for i in range(W)])
    if any([any([c>K for c in r]) for r in row_list]):
        continue
    cnt = [0]*len(row_list)
    tmp = [0]*len(row_list)
    for i in range(W):
        for j in range(len(row_list)):
            cnt[j] += row_list[j][i]
            tmp[j] = row_list[j][i]
        if any([c>K for c in cnt]):
            cut += 1
            cnt = tmp[:]
    ans = min(ans,cut)
print(ans)
