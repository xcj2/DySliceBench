import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**2) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,a,b,c = li()
l = [ni() for _ in range(n)]

ans = 10**18

for i in range(4**n):
    cur = i
    cnt = {i: [] for i in range(4)}
    
    for bi in l:
        cnt[cur%4].append(bi)
        cur //= 4
    
    
    if len(cnt[1]) * len(cnt[2]) * len(cnt[3]) == 0:
        continue
    
    ans = min(ans, abs(a-sum(cnt[1]))\
                  + abs(b-sum(cnt[2]))\
                  + abs(c-sum(cnt[3]))\
                  + 10*(n - len(cnt[0]) -3))
    
print(ans)