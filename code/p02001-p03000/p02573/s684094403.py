N, M = map(int, input().split())

#UnionFind木を使う

p = [-1] * N

def find(x):
    #print(x)
    if p[x] < 0:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    p[y] += p[x] #木のサイズをマイナスの方向に増やして記録していく
    p[x] = y
    return

def size(x):
    return -p[p[x]]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    union(a, b)

#print(p)
# xが子の場合，p[x] = 親（根，root）
# xが親の場合，p[x] = -1 * 木のサイズ

ans = max(map(size, range(N)))

print(ans)