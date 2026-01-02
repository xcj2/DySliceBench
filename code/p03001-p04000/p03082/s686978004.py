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

from collections import defaultdict

MOD = 10**9+7

n,x = li()
s = list(li())
s.sort(reverse=True)

dd = defaultdict(int)

dd[x] = 1

for i in range(n):
    nexdd = defaultdict(int)
    
    for k, v in dd.items():
        nexdd[k] += dd[k] * (n-i-1)
        nexdd[k] %= MOD
        
        nexdd[k%s[i]] += dd[k]
        nexdd[k%s[i]] %= MOD
        
    dd = nexdd
    
ans = 0
for k,v in dd.items():
    ans += k*v
    ans %= MOD
    
print(ans)