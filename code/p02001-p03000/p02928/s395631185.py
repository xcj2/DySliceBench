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
MOD = 10**9 + 7

ans = 0
for i, ai in enumerate(a):
    for j, aj in enumerate(a):
        if ai > aj:
            if j < i:
                ans += ((k-1)*k // 2)
            else:
                ans += ((k+1)*k // 2)

            ans %= MOD


print(ans % MOD)