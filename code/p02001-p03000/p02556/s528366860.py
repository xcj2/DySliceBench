import sys

sys.setrecursionlimit(10**6)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

n=II()
xy=[]
for _ in range(n):
    u,v=MI()
    xy.append((u+v,u-v))
xy.sort()
l=xy[0][0]
t=b=xy[0][1]
ans=0
for x,y in xy:
    ans=max(ans,x-l,t-y,y-b)
    t=max(t,y)
    b=min(b,y)
print(ans)
