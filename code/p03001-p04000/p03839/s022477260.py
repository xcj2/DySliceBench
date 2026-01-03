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

n, k = li()
a = list(li())
INF = 10**18

cum_raw = [0]*(n+1)
cum_max = [0]*(n+1)

for i in range(n):
    cum_raw[i+1] = cum_raw[i] + a[i]
    cum_max[i+1] = cum_max[i] + (0 if a[i] < 0 else a[i])

ans = -INF

for i in range(n-k+1):
    white_zone = (cum_max[i] - cum_max[0]) + (cum_max[n] - cum_max[i+k])
    black_zone = (cum_raw[i+k] - cum_raw[i])
    ans = max(ans, white_zone)
    ans = max(ans, white_zone + black_zone)

print(ans)