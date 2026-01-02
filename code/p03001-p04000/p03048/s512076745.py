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

r,g,b,n = li()
ans = 0
for ri in range(0, n+1, r):
    for gi in range(0, n+1, g):
        if ri+gi > n:
            continue
        elif (n-ri-gi) % b:
            continue

        ans += 1

print(ans)