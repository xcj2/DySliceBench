import numpy as np

#root = {}でいけるか

def find(a):
    if a==root[a]: return a
    else: root[a] = find(root[a]) ; return root[a]
    
def unite(a,b):
    ra,rb = find(a),find(b)
    if ra==rb : return
    else: root[ra] = rb
    
def same(a,b): return find(a)==find(b)

n,m =  map(int,input().split())
ab = np.array([list(map(int,input().split())) for i in range(m)])
a,b = ab.T[0]-1, ab.T[1]-1

ans = 0
for i in range(m):
    root = list(range(n))
    connect = 0
    for j in range(m):
        if i==j: continue
        if not same(a[j],b[j]): unite(a[j],b[j]); connect += 1
    ans += 0 if connect==n-1 else 1
    
print(ans)
