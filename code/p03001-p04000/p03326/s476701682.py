import sys
input = sys.stdin.readline
N,M = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(N)]

def score(x): return abs(x[0])+abs(x[1])+abs(x[2])
def add(a, b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def score2(x,c): return x[0]*c[0] + x[1]*c[1] + x[2]*c[2]
def key(c): return lambda x: score2(x,c)

def solve(c):
    A = sorted(xyz, key=key(c))
    rslt=(0,0,0)
    for i in range(M):
        rslt = add(rslt, A[i])
    return score(rslt)

ans=0
for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            ans=max(ans,solve((i,j,k)))
print(ans)