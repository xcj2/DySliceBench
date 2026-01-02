def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)
    
K = INT()

memo = []
for i in range(K):
    memo2 = []
    for j in range(K):
        memo2.append([-1] * K)
    memo.append(memo2)


def memorize(i, j, k, a):
    memo[i-1][j-1][k-1] = a

ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            if memo[i-1][j-1][k-1] == -1:
                a = gcd(i, j, k)
                memorize(i,j,k, a)
                memorize(i,k,j, a)
                memorize(j,i,k, a)
                memorize(j,k,i, a)
                memorize(k,i,j, a)
                memorize(k,j,i, a)
                ans += a
            else:
                ans += memo[i-1][j-1][k-1]
print(ans)
