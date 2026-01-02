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
a = list(li_())
b = list(li())
c = list(li())

ans = 0
bef = -10

for i, ai in enumerate(a):
    ans += b[ai]
    if bef == (ai - 1):
        ans += c[ai - 1]

    bef = ai

print(ans)