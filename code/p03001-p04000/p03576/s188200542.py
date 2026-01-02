import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,k = li()
x = []
y = []
points = [tuple(li()) for _ in range(n)]
for i in range(n):
    x.append(points[i][0])
    y.append(points[i][1])
    
x.sort()
y.sort()

ans = (x[-1]-x[0]) * (y[-1]-y[0])
for u,xs in enumerate(x[:-1]):
    for xt in x[u+1:]:
        for v,ys in enumerate(y[:-1]):
            for yt in y[v+1:]:
                area = (xt-xs) * (yt-ys)
                inner = 0
                for xi,yi in points:
                    if xs<=xi<=xt and ys<=yi<=yt:
                        inner += 1
                        
                if inner >= k:
                    ans = min(ans,area)
                    
                    
print(ans)