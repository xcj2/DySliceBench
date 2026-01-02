# union-find
# こういう問題のときにUnion-Findなのか幅優先探索なのか深さ優先探索なのか迷う。
# ちなみに解説PDFはUnion-Findを挙げている。

n, m = map(int, input().split())

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]

def unite(x, y):
    x = find_root(x)
    y = find_root(y)
    if(x == y):
        return 0

    if rank[x] < rank[y]:
        par[x] = y

        temp = size[x] * size[y]
        size[y] = size[x] + size[y]
    else:
        par[y] = x
        if (rank[x] == rank[y]):
            rank[x] += 11

        temp = size[x] * size[y]
        size[x] = size[x] + size[y]
    return temp

def is_same(x,y):
    return find_root(x) == find_root(y)

# par = [0]*n
par = list(range(n))
rank = [0]*n
size = [1]*n

init_nums = list(map(int, input().split()))

edges = [list(map(int, input().split())) for _ in range(m)]
edges = [[b[0]-1, b[1]-1] for b in edges] #1-idx -> 0-idx

for b in range(m):
    unite(edges[b][0] , edges[b][1])

ans = 0
for i in range(n):
    num = init_nums[i]
    # i+1 が init_numの中でi+1と同じグループだったら
    if is_same(i, num - 1):
        ans += 1

print(ans)
