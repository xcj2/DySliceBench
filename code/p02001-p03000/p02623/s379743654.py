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

N,M,K = LI()
A = LI()
B = LI()

cusumA = [A[0]]*N
cusumB = [B[0]]*M

for i in range(1,N):
    cusumA[i] = cusumA[i-1]+A[i]

for i in range(1,M):
    cusumB[i] = cusumB[i-1]+B[i]

ans = 0
for i in range(N):
    left = K-cusumA[i]
    if left < 0:
        break
    p = bisect_right(cusumB,left)
    num = i+1+p
    if num > ans:
        ans = num

p = bisect_right(cusumB,K)
if p > ans:
    ans = p

print(ans)