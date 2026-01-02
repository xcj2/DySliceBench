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

from math import sqrt

n = ni()
ans = n-1

for i in range(2, int(sqrt(n)) + 2):
    if n == i:
        break
    if n % i == 0:
        ans = min(ans, i + n//i - 2)

print(ans)