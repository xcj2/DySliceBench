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

ans = 0
for i in range(k+1, n+1):
    ans += (n+1)//i * (i-k)
    ans += max(0, (n+1)%i - k)

if k == 0:
    ans -= n

print(ans)