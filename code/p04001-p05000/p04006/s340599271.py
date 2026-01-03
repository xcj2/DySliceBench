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

n,x = li()
a = list(li())

mins = [ai for ai in a]
a = a+a

ans = 10**18
for k in range(n):
    for i in range(n,2*n):
        mins[i-n] = min(mins[i-n], a[i-k])
        
    ans = min(ans, sum(mins) + x*k)
    
print(ans)