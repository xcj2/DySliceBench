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
a = list(li())
ans = 0

for i in range(n-2):
    p0, p1, p2 = a[i:i+3]
    st = sorted([p0, p1, p2])

    if p1 == st[1]:
        ans += 1

print(ans)