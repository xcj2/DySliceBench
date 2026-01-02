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

btc = 380000

n = ni()

ans = 0
for _ in range(n):
    s = ls()
    num = float(s[0])
    typ = s[1]
    
    if typ == "JPY":
        ans += num
    else:
        ans += num * btc
        
print(ans)