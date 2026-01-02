import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N,K=LI()
S=input()

cnt = 0
lst = None
RNGS=[]
for i in range(N):
    if lst and lst != S[i]:
        RNGS.append((lst, cnt))
        cnt = 0
    cnt += 1
    lst = S[i]
RNGS.append((lst, cnt))

# print(RNGS)

mod_cnt = 0
if len(RNGS) >= 3:
    for i in range(0, len(RNGS)-2, 2):
        if mod_cnt < K:
            lr, num = RNGS[i+1]
            lr = 'L' if lr ==  'R' else 'R'
            mod_cnt += 1
            RNGS[i+1] = (lr, num)

# print(RNGS)
if mod_cnt < K:
    print(len(S) - 1)
else:
    prev = None
    res = 0
    for i in range(len(RNGS)):
        lr, num = RNGS[i]
        res += num
        if not prev or prev != lr:
            res -= 1
        prev = lr
    print(res)
