def root(x):
    if parent[x] == x:
        return(x)
    else:
        parent[x] = root(parent[x])
        return(parent[x])


def same(x, y):
    return(root(x) == root(y))


def union(x, y):
    x = root(x)
    y = root(y)
    if(x == y):
        return False

    parent[x] = min(x, y)
    parent[y] = min(x, y)
    return True





H, W = map(int, input().split())
S = [input() for _ in range(H)]

parent = [i for i in range(H*W)]

neighbor = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for h in range(H):
    for w in range(W):
        for px, py in neighbor:
            tx = w + px
            ty = h + py
            # print(tx, ty, tx < 0 or tx >= w or ty < 0 or ty >= h)
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            
            # print({S[h][w], S[ty][tx]})
            if {S[h][w], S[ty][tx]} == {"#", "."}:
                union(h*W+w,ty*W+tx)

ans = {root(r):{"#":0, ".":0} for r in parent}
for i in range(H*W):
    ans[root(i)][S[i//W][i%W]] += 1
# print(parent)
# print(ans)

print(sum(v["#"]*v["."] for v in ans.values()))