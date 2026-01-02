import sys
from bisect import bisect_right

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N, D, A = MI()
monsters = list()
for i in range(N):
    x, h = MI()
    monsters.append((x, (h + A - 1) // A))
monsters.sort()

X = [x for x, h in monsters]
ub = [0] * N
for i, x in enumerate(X):
    ub[i] = bisect_right(X, x + 2 * D)

dmg = [0] * N
accum = 0
ans = 0
for i, (x, h) in enumerate(monsters):
    h = h - max(0, accum + dmg[i])
    if h > 0:
        ans += h
        dmg[i] += h
        if ub[i] < N:
            dmg[ub[i]] -= h
    accum += dmg[i]
print(ans)
