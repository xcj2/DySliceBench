import sys
sys.setrecursionlimit(1000000)

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

n, q = map(int, input().split())
root = [i for i in range(n)]
rank = [1 for _ in range(n)]

for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        unite(u, v)
    else:
        print(1 if same(u, v) else 0)