N,M,K = map(int,input().split())

# Union Find

# xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        # sizeの大きいほうがx
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


# xとyが同じ集合に属するかの判定
def same(x, y):
    return find(x) == find(y)


# xが属する集合の個数
def size(x):
    return -par[find(x)]

# 初期化
# 根なら-size,子なら親の頂点
par = [-1]*(N+1)


friend_list = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    unite(A,B)
    friend_list[A].append((B))
    friend_list[B].append((A))

block_list = [[] for _ in range(N+1)]
for _ in range(K):
    C, D = map(int, input().split())
    block_list[C].append(D)
    block_list[D].append(C)

anslist = [0]*(N)
for i in range(1,N+1):

    block_and_connect = 0
    for hito in block_list[i]:
        if same(hito,i):
            block_and_connect += 1
    ans = size(i) - 1 - len(friend_list[i]) - block_and_connect
    anslist[i-1] = ans
print(*anslist)

