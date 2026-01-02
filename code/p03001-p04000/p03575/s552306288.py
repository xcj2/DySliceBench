n,m = map(int,input().split())
d = []
for i in range(m):
    a,b = map(int,input().split())
    a,b = a-1, b-1
    d.append((a,b))
#print(d)
pa = None

def root(a):
    if pa[a] == a:
        return a
    else:
        pa[a] = root(pa[a])
        return pa[a]
def is_same(a,b):
    return root(a) == root(b)
def unite(a,b):
    aa = root(a)
    bb = root(b)
    if aa == bb:
        return
    pa[aa] = bb

ans = 0
for i in range(m):
    pa = [x for x in range(n)]
    for j,v in enumerate(d):
        #(i,j,v)
        if i == j:continue
        a,b = v
        unite(a,b)
    a,b = d[i]
    if not is_same(a,b):
        ans +=1
print(ans)