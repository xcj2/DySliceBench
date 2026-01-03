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

n = int(input())
root = [i for i in range(n)]
rank = [1 for _ in range(n)]
s, t = [], []
for i in range(n):
    x, y = map(int, input().split())
    s.append([x, i])
    t.append([y, i])
s.sort()
t.sort()
u = []
for i in range(n - 1):
    u.append([abs(s[i][0] - s[i + 1][0]), s[i][1], s[i + 1][1]])
    u.append([abs(t[i][0] - t[i + 1][0]), t[i][1], t[i + 1][1]])
u.sort()
c = 0
ans = 0
for v in u:
    if not same(v[1], v[2]):
        unite(v[1], v[2])
        c += 1
        ans += v[0]
    if c == n - 1:
        break
print(ans)