n,m = map(int,input().split())
e = [0]*m

for i in range(m):
    a,b = map(int,input().split())
    e[m-1-i] = [a-1,b-1]

root = [-1]*n
rank = [0]*n
    
def find(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def unite(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    elif rank[x] > rank[y]:
        root[x] += root[y]
        root[y] = x
    else:
        root[y] += root[x]
        root[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def same(x,y):
    return find(x) == find(y)

def cnt(x):
    return root[find(x)]


ans = [0]*m
ans[0] = n*(n-1) // 2

for i in range(1,m):
    if same(e[i-1][0],e[i-1][1]):
        ans[i] = ans[i-1]
    else:
        ans[i] = ans[i-1] - cnt(e[i-1][0]) * cnt(e[i-1][1])
    unite(e[i-1][0],e[i-1][1])

for i in range(m):
    print(ans[m-1-i])