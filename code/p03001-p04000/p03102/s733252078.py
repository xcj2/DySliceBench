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

n,m,c = li()
b = list(li())
a = [list(li()) for _ in range(n)]

ans = 0
for ai in a:
    if sum([aij*bi for aij, bi in zip(ai, b)]) + c > 0:
        ans += 1
print(ans)