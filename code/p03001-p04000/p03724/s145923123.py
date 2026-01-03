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

from collections import defaultdict

n,m  = li()
query = []
for _ in range(m):
    mi,ma = li()
    if mi > ma:
        mi,ma = ma,mi
        
    query.append((mi,ma))

root = defaultdict(list)
for l,r in query:
    root[l].append(r)


even = -1
odd = -1
for k, v in root.items():
    if len(v)%2 == 0 and even == -1:
        even = k
        
    elif len(v)%2 == 1 and odd == -1:
        odd = k

# 偶数個つながっているノードをルートに
top = even
dist = [0]*n
for l,r in query:
    if l==top:
        dist[r-1] += 1
    
    elif r==top:
        dist[l-1] += 1
    
    else:
        dist[r-1] += 1
        dist[l-1] += 1
        
exist = False
if top != -1 and all([disti % 2 == 0 for disti in dist]):
    exist = True
    

# 奇数個つながっているノードをルートに
top = odd
dist = [0]*n
for l,r in query:
    if l==top:
        dist[r-1] += 1
    
    elif r==top:
        dist[l-1] += 1
    
    else:
        dist[r-1] += 1
        dist[l-1] += 1
        
if top != -1 and all([disti % 2 == 0 for disti in dist]):
    exist = True

if exist:
    print("YES")
else:
    print("NO")   