def get_root(s):
    if s != root[s]:
        root[s] = get_root(root[s])
        return root[s]
    return s

def unite(s, t):
    root_s = get_root(s)
    root_t = get_root(t)
    if not root_s == root_t:
        if rank[s] == rank[t]:
            root[root_t] = root_s
            rank[root_s] += 1
        elif rank[s] > rank[t]:
            root[root_t] = root_s
        else:
            root[root_s] = root_t

def same(s, t):
    if get_root(s) == get_root(t):
        return True
    else:
        return False

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
ans = 0
for i in range(m):
    root = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    for j in range(m):
        if not i == j:
            unite(l[j][0] - 1, l[j][1] - 1)
    c = 0
    for j in range(n - 1):
        if not same(j, j + 1):
            c = 1
            break
    if c == 1:
        ans += 1
print(ans)