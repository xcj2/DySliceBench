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


m, d = li()
ans = 0
for mi in range(1, m+1):
    for di in range(1, d+1):
        if di%10 >= 2 and di//10 >= 2:
            if (di%10) * (di//10) == mi:
                ans += 1

print(ans)