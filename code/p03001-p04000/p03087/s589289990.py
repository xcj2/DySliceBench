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

n,q = li()
s = lc()

cnt = [0]*(n)

for i in range(1,n):
    if s[i-1] == "A" and s[i] == "C":
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]
        
for _ in range(q):
    l,r = li_()
    print(cnt[r]-cnt[l])
    