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

cum = [0]
for ai in a:
    cum.append(cum[-1] + ai)

pool = []
for i in range(n+1):
    for j in range(i+1, n+1):
        pool.append(cum[j] - cum[i])

MAX_BIT = 41
ans = 0
for bit in range(MAX_BIT, -1, -1):
    new_pool = []
    for poli in pool:
        if poli & (1<<bit):
            new_pool.append(poli)

    if len(new_pool) >= k:
        ans += (1<<bit)
        pool = new_pool

print(ans)