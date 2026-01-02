import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from bisect import bisect_left, bisect_right

n = ni()
a = sorted(list(li()))
b = sorted(list(li()))
c = sorted(list(li()))

ans = 0
for bi in b:
    ans += bisect_left(a,bi)*(n-bisect_right(c,bi))
    
print(ans)