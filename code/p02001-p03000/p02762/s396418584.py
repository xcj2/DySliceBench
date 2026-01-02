def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y: return False
    #sizeの大きいほうがx
    if par[x] > par[y]: x,y = y,x
    par[x] += par[y]
    par[y] = x
    return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

n, m, k = map(int, input().split())
friend = [[] for _ in range(n)]
enemy = [[] for _ in range(n)]
par = [-1]*n


for _ in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)
for _ in range(k):
    a, b = map(int, input().split())
    enemy[a-1].append(b-1)
    enemy[b-1].append(a-1)
ans = []
for i in range(n):
    block = 0
    for j in enemy[i]:
        if same(i, j): block += 1
    ans.append(size(i)-len(friend[i])-block-1)
print(*ans)