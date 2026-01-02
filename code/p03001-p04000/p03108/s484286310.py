#root:根
#find:根を考える
#rank:木の深さ
#size:size[i]:iを根とするグループのサイズ

def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])

def unite(x,y):
    x = find(x)
    y = find(y)    
    if x != y:
        if rank[x] < rank[y]:
            root[x] = y
            size[y] += size[x]
        else:
            root[y] = x
            size[x] += size[y]
            if rank[x]==rank[y]:
                rank[x] += 1

def same(x,y):
    return find(x) == find(y)

n,m = map(int,input().split())

root = [0]*n
for i in range(n):
    root[i] = i
rank = [1]*n
size = [1]*n

edge = [[int(i)-1 for i in input().split()] for i in range(m)]
edge = edge[::-1]

res = []
for i in range(m):
    r1 = find(edge[i][0])
    r2 = find(edge[i][1])
    if r1 == r2:
        res.append(0)
    else:
        res.append(size[r1]*size[r2])
        unite(r1,r2)
        
ans = 0
for i in range(m):
    ans += res[m-1-i]
    print(ans)