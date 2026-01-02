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

n = ni()
march = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(n):
    s = lc()
    if s[0] in march.keys():
        march[s[0]] += 1
        
ans = 0
vals = list(march.values())
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans += vals[i]*vals[j]*vals[k]
            
print(ans)