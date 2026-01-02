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

S=input()
T=input()
lenS=len(S)

NX=[[-1]*26 for _ in range(len(S))]

for i in range(len(S)*2-1)[::-1]:
    idx = i%lenS
    idx2 = (i+1)%lenS
    for j in range(26):
        if NX[idx2][j] != -1:
            NX[idx][j] = NX[idx2][j] + 1
    NX[idx][ord(S[idx2])%26] = 1

# for lis in NX:
#     print(lis)
# for c in S:
#     print(ord(c)%26, end=" ")
# print("")

res = 0
prev=lenS-1
for c in T:
    v = NX[prev][ord(c)%26]
    if v == -1:
        print(-1)
        exit()
    else:
        res += v
        prev = (prev + v)%lenS

print(res)
