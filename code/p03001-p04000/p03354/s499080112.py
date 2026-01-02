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
p = list(map(int, input().split()))
root = [i for i in range(n)]
rank = [1 for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    unite(x - 1, y - 1)
ans = 0
for i in range(n):
    if get_root(i) == get_root(p[i] - 1):
        ans += 1
print(ans)