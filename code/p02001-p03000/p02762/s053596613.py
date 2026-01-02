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
            union_count[root_s] += union_count[root_t]
        elif rank[s] > rank[t]:
            root[root_t] = root_s
            union_count[root_s] += union_count[root_t]
        else:
            root[root_s] = root_t
            union_count[root_t] += union_count[root_s]

def same(s, t):
    if get_root(s) == get_root(t):
        return True
    else:
        return False

n, m, k = map(int, input().split())
root = [i for i in range(n)]
rank = [1 for _ in range(n)]
union_count = [1 for _ in range(n)]
friend_count = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    unite(a - 1, b - 1)
    friend_count[a - 1] += 1
    friend_count[b - 1] += 1
ans = [-1] * n
for _ in range(k):
    c, d = map(int, input().split())
    if same(c - 1, d - 1):
        ans[c - 1] -= 1
        ans[d - 1] -= 1
for i in range(n):
    r = get_root(i)
    ans[i] += union_count[r] - friend_count[i]
print(" ".join(map(str, ans)))