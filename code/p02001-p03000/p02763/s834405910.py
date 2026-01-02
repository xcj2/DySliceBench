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

N = I()
S = list(ST())
Q = I()
bits=[[0]*(N+1) for _ in range(26)]

def ctoi(c): #アルファベットを0-25の数字に変換
    return ord(c)-97

def query(pos): #各文字について1-pos番目までの文字数をカウント
    ret = [0]*26
    for i in range(26):
        tmp = 0
        p = pos
        while p>0:
            tmp += bits[i][p]
            bit_len = p&(-p) #p&(-p)は1のたつ最小桁であり、今の区間の長さをあらわす
            p -= bit_len #つぎに足すべき塊の番号は、今の値から区間の長さを引くとでる
        ret[i] = tmp #アルファベットiの1-posまでの出現回数
    return ret

def update(pos, a, x): #a番目のアルファベットについてpos番目の要素の値を更新
    while pos <= N:
        bits[a][pos] += x
        pos += pos&(-pos)

for i in range(N):
    update(i+1, ctoi(S[i]),1)
for _ in range(Q):
    q = LST()
    if q[0]=='1':
        i = int(q[1])
        c = q[2]
        if S[i-1]==c:
            continue
        update(i, ctoi(S[i-1]), -1) #S[i-1]のi番目に1が立っているが、これを下ろして削除を表現
        #O(logN)で削除が完了
        update(i, ctoi(c), 1)
        S[i-1] = c
    else:
        ans = 0
        l = int(q[1])
        r = int(q[2])
        r_sum = query(r)
        l_sum = query(l-1)
        for i in range(26):
            if r_sum[i]-l_sum[i] > 0:
                ans += 1
        print(ans)
