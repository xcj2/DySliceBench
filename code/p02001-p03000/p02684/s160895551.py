import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()
A = LMI()

from math import log2

# next[k][i] := i番目の要素の2^k個次の要素
next = [[0] * N for _ in range(int(log2(K)) + 1)]

# 構築 O(NlogK)
next[0] = [a - 1 for a in A]
for k in range(int(log2(K))):
    for i in range(N):
        # i番目の要素の2^(k+1)個次の要素 := next[k][i](i番目の要素の2^k個次の要素)の2^k個先
        next[k + 1][i] = next[k][next[k][i]]

# クエリ O(logK)
# p番目の要素のQ個次の要素を求める
p = 0
for i in reversed(range(int(log2(K)) + 1)):
    if (K >> i) & 1:
        p = next[i][p]
print(p + 1)
