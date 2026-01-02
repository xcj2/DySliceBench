from operator import mul
from functools import reduce
def comb2(n,r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under
def comb3(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, M, K = LI()

cou = int(0)
#maxL = N + M -2
L = int(0)
#距離i+1の組み合わせ

#for i in range(maxL):
for j in range(N):
    L += (N - j - 1) * (M ** 2) * (j + 1)
for j in range(M):
    L += (M - j - 1) * (N ** 2) * (j + 1)
#    for j in range(i+2):
#        if i>1 and i+1>j>0:
#            L[i] += max((N-j)*(M-(1+i)+j),0)*(i+1)*2
#        else:
#            L[i] += max(((N - j) * (M - (1 + i) + j)), 0) * (i + 1)

cou = comb3(N*M-2,K-2)%mod

ans = cou *L%mod

print(ans)