def find(n):
    if root[n] < 0:
        return n
    else:
        root[n] = find(root[n])
        return root[n]
    
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if root[x] > root[y]:
        x, y = y, x
    
    root[x] += root[y]
    root[y] = x
    
def size(x):
    return -root[find(x)]

def same(x,y):
    return find(x) == find(y)

def member(x):
    rt = find(x)
    return [i for i in range(n) if find(i) == rt]

def roots():
    return [i for i, x in enumerate(root) if x < 0]

def member_count(x):
    return len(roots())

def all_group_members():
    return {r: member(r) for r in roots()}

n , m = map(int,input().split())
root = [-1 for i in range(n)]
ans = [0 for i in range(m)]
ans[m-1] = n*(n-1)//2
hasi = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(m)]
for i in reversed(range(m-1)):
    a , b = hasi[i+1]
    if same(a,b):
        ans[i] = ans[i+1]
    else:
        ans[i] = ans[i+1] - size(a)*size(b)
        unite(a,b)
for i in range(m):
    print(ans[i])