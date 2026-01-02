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

from bisect import bisect_left

n = ni()
l = list(li())

l.sort()

ans = 0

for i in range(n):
    for j in range(i+1, n):
        k = bisect_left(l, l[i] + l[j])
        ans += (k - j - 1)

print(ans)
