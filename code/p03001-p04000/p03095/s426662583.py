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

from collections import Counter

n = ni()
s = ns()

MOD = 10**9+7

cnt = Counter(s)
ans = 1

for key, val in cnt.items():
    ans *= (val+1)
    ans %= MOD
    
ans -= 1
if ans < 0:
    ans += MOD
    
print(ans)