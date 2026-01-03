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

n = ni()

ans = 0
plus = 0
a = [ni() for _ in range(n)]

for ai in a:
    ans += ((ai+plus) // 2)
    plus = (ai+plus) % 2 if ai > 0 else 0

print(ans)