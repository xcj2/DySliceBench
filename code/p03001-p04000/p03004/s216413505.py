INF = float('inf')
from collections import defaultdict
N = int(input())
dx = defaultdict(list)
dy = defaultdict(list)
for i in range(N):
    x,y,d = input().split()
    x = int(x)
    y = int(y)
    dx[d].append(x)
    dy[d].append(y)

mxl = INF
if 'L' in dx:
    mxl = min(dx['L'])
mxr = INF
if 'R' in dx:
    mxr = min(dx['R'])
mxud = INF
if 'U' in dx:
    mxud = min(dx['U'])
if 'D' in dx:
    mxud = min(min(dx['D']),mxud)
Mxl = -INF
if 'L' in dx:
    Mxl = max(dx['L'])
Mxr = -INF
if 'R' in dx:
    Mxr = max(dx['R'])
Mxud = -INF
if 'U' in dx:
    Mxud = max(dx['U'])
if 'D' in dx:
    Mxud = max(max(dx['D']),Mxud)
myu = INF
if 'U' in dy:
    myu = min(dy['U'])
myd = INF
if 'D' in dy:
    myd = min(dy['D'])
mylr = INF
if 'L' in dy:
    mylr = min(dy['L'])
if 'R' in dy:
    mylr = min(min(dy['R']),mylr)
Myu = -INF
if 'U' in dy:
    Myu = max(dy['U'])
Myd = -INF
if 'D' in dy:
    Myd = max(dy['D'])
Mylr = -INF
if 'L' in dy:
    Mylr = max(dy['L'])
if 'R' in dy:
    Mylr = max(max(dy['R']),Mylr)

def xmin(t):
    return min(mxl-t,mxr+t,mxud)

def xmax(t):
    return max(Mxl-t,Mxr+t,Mxud)

def ymin(t):
    return min(myu+t,myd-t,mylr)

def ymax(t):
    return max(Myu+t,Myd-t,Mylr)

cand = [0,(mxl-mxr)/2,mxl-mxud,mxud-mxr,(Mxl-Mxr)/2,Mxl-Mxud,Mxud-Mxr,(myd-myu)/2,mylr-myu,myd-mylr,(Myd-Myu)/2,Mylr-Myu,Myd-Mylr]

ans = INF
for t in cand:
    if t < 0:
        continue
    ans = min(ans,(xmax(t)-xmin(t))*(ymax(t)-ymin(t)))
print(ans)