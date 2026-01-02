import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# Kを二進数表記する
# Kでbit=1の桁でbit orを0にすると，それ以下の桁は何でもよい

N,K = LI()
A0,B0 = LIR(N,2)

A = []
B = []
for i in range(N):
    if A0[i] <= K:
        A.append(A0[i])
        B.append(B0[i])

Ks = format(K,'b')
L = len(Ks)
last_zero = -1
for i in range(L)[::-1]:
    if Ks[i] == '0':
        last_zero = i
        break

if last_zero == -1:
    print(sum(B))
else:
    zeros = []
    must_zero = []
    for i,s in enumerate(Ks):
        if s == '1':
            must_zero.append(zeros+[i])
        else:
            zeros.append(i)
            if i == last_zero:
                must_zero.append(zeros)
                break
    ans = 0
    for zl in must_zero:
        temp = 0
        for a,b in zip(A,B):
            flag = False
            for i in zl:
                if a & 1<<(L-i-1) != 0:
                    flag = True
                    break
            if not flag:
                temp += b
        if temp > ans:
            ans = temp
    print(ans)