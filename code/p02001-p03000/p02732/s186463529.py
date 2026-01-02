import sys
from collections import Counter
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return list(map(int, input().split()))

n = INT()
a = LIST()
c = list(set(a))
b = [0 for _ in range(n + 1)]
for i in range(n):
    b[a[i]] += 1
d = [0 for _ in range(n + 1)]
e = [0 for _ in range(n + 1)]
for i in range(n + 1):
    if b[i] >= 2:
        d[i] = b[i] * (b[i] - 1) // 2
    if b[i] >= 3:
        e[i] = (b[i] - 1) * (b[i] - 2) // 2
sd = sum(d)
se = sum(e)
for k in range(n):
    ans = sd - d[a[k]] + e[a[k]]
    print(ans)
