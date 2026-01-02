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

maxa = max(a)

a.remove(maxa)

half = maxa / 2
minabs_from_half = 10**18

ans = -1
for ai in a:
    if abs(half - ai) < minabs_from_half:
        ans = ai
        minabs_from_half = abs(half - ai)

print(maxa, ans)