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

# mの約数を求める
i = 1
div = []
while i*i <= m:
    if m%i == 0:
        div.append(i)
        div.append(m//i)
    i += 1
    
ans = 1
for d in div:
    if m//d >= n:
        ans = max(ans, d)
        
print(ans)