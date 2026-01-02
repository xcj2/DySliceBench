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

N=II()

mp={}

for i in range(N):
    key = "".join(sorted(input()))
    if key in mp:
        mp[key] += 1
    else:
        mp[key] = 1

res = 0
for k, v in mp.items():
    if v >= 2: res += (v * (v-1) // 2)

print(res)
