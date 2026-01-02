import sys
import math
from collections import defaultdict

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

N,M,V,P = LI()
A = LI()

A.sort(reverse=True)
cumA = [A[0]]
for i in range(1,N):
    cumA.append(cumA[-1]+A[i])

ans = P
if V < P:
    for i in range(P,N):
        if A[P-1] <= A[i]+M:
            ans += 1
else:
    for i in range(P,N):
        if A[i]+M < A[P-1]:
            continue
        cum = cumA[i-1]-cumA[P-2] if P >= 2 else cumA[i-1]
        cap = (i-P+1)*(M+A[i]) - cum + M*(N-i-1)
        if cap >= M*(V-P):
            ans += 1

print(ans)