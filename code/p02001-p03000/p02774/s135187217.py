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

N,K = MI()
A = LI()
minus,zero,plus = [], [], []
for i in A:
    if i<0:
        minus.append(i)
    elif i==0:
        zero.append(i)
    else:
        plus.append(i)
m = len(minus)
p = len(plus)
z = len(zero)
minus.sort()
plus.sort()

def count_lower_negpos(v): #pos*negでv以下のペアを数える
    if not minus or not plus:
        return 0
    m_idx = 0
    p_idx = 0
    ans = 0
    while True:
        val = minus[m_idx]*plus[p_idx]
        if val < v:
            ans += p - p_idx
            m_idx += 1
            if m_idx>m-1:
                break
        else:
            p_idx += 1
            if p_idx>p-1:
                break
    return ans

def count_lower_pospos(v): #pos同士でv以下のペアを数える
    if not plus:
        return 0
    left = 0
    right = p-1
    ans = 0
    while True:
        val = plus[left]*plus[right]
        if val < v:
            ans += right - left
            left += 1
            if left>=right:
                break
        else:
            right -= 1
            if left>=right:
                break
    return ans

def count_lower_negneg(v): #neg同士でv以下のペアを数える
    if not minus:
        return 0
    left = 0
    right = m-1
    ans = 0
    while True:
        val = minus[left]*minus[right]
        if val < v:
            ans += right - left
            right -= 1
            if left>=right:
                break
        else:
            left += 1
            if left>=right:
                break
    return ans


if K <= m*p: #答えがマイナス
    l = -10**18-5
    r = 0
    while l+1<r:
        x = (l+r)//2
        if count_lower_negpos(x) < K:
            l = x
        else:
            r = x
    print(l)


elif K <= m*p+z*(m+p)+z*(z-1)//2: #答えがゼロ
    print(0)

else: #答えがプラス
    K = K - (m*p+z*(m+p)+z*(z-1)//2)
    l = 0
    r = 10**18+5
    while l+1<r:
        x = (l+r)//2
        if count_lower_pospos(x)+count_lower_negneg(x) < K:
            l = x
        else:
            r = x
    print(l)
