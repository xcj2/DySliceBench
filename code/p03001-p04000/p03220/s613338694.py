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
t,a = li()
h = list(li())

ans = -1
res = 10**18
for i,hi in enumerate(h):
    if abs(a-(t-0.006*hi)) < res:
        res = abs(a-(t-0.006*hi))
        ans = i+1
        
print(ans)