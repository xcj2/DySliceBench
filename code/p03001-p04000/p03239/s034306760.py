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

n,t = li()
ct = []
for _ in range(n):
    ct.append(list(li()))
    
ans = 10**18
for ci, ti in ct:
    if ti <= t:
        ans = min(ans, ci)
        
if ans == 10**18:
    print("TLE")
else:
    print(ans)