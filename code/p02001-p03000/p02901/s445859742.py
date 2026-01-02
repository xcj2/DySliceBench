import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, m = li()
inf = float('inf')

a = []
b = []
c = []
for _ in range(m):
    ai, bi = li()
    ci = list(li_())
    a.append(ai)
    b.append(bi)
    state = 0
    for cij in ci:
        state += pow(2, cij)
    c.append(state)


dp = [inf]*(1<<n)
dp[0] = 0

for state in range(1<<n):
    for i in range(m):
        dp[state | c[i]] = min(dp[state] + a[i], dp[state | c[i]])

print(dp[-1] if dp[-1] != inf else -1)