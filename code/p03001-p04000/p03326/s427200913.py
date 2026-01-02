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
xyz = []
for _ in range(n):
    xyz.append(tuple(li()))
    
ans = -10**18
for i in range(-1,2,2):
    for j in range(-1,2,2):
        for k in range(-1,2,2):
            temp = sorted([i*x+j*y+k*z for x,y,z in xyz], reverse=True)
            ans = max(ans, sum(temp[:m]))
            
print(ans)