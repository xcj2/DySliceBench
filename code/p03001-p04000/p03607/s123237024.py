import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

n = ni()
a = [ni() for _ in range(n)]

cnt = Counter(a)

ans = 0
for ci in cnt.values():
    if ci % 2 == 1:
        ans += 1
        
print(ans)