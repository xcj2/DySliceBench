import sys
sys.setrecursionlimit(300000)
from itertools import accumulate

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M, K = MI()
A = LMI()
B = LMI()

a = list(accumulate([0, *A]))
b = list(accumulate([0, *B]))

ans = 0
j = M
for i in range(N + 1):
    if a[i] > K:
        break
    while b[j] > K - a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
