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

n,m = li()

cnt = [0]*n
for _ in range(m):
    a,b = li_()
    cnt[a] += 1
    cnt[b] += 1
    
exist = True
for c in cnt:
    if c%2:
        exist = False
        break

if exist:
    print("YES")
else:
    print("NO")