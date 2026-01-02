import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
S = input()

d = defaultdict(int)
for c in S:
    d[c] += 1
plus = d['R'] * d['G'] * d['B']

minus = 0
for j in range(1, N - 1):
    for l in range(1, N):
        i, k = j - l, j + l
        if i < 0 or k > N - 1:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            minus += 1

print(plus - minus)
