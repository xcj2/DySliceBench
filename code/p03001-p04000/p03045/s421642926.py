def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if rank[x] == rank[y]:
        root[y] = x
        rank[x] += 1
    elif rank[x] > rank[y]:
        root[y] = x
    elif rank[x] < rank[y]:
        root[x] = y
    
n,m = map(int, input().split())
root = [i for i in range(n)]
rank = [0 for i in range(n)]

for i in range(m):
    x, y, z = [int(i)-1 for i in input().split()]
    if not same(x,y):
        unite(x,y)
    
for i in range(n):
    find(i)

print(len(list(set(root))))
