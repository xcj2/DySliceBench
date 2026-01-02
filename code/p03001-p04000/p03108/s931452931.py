def find_index_by_value(a, val):
    for i, items in enumerate(a):
        if val in items:
            return i
    return -1


def num_reachable(n):
    return n * (n - 1) // 2


n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

size = [1 for _ in range(n + 1)]
group = [i for i in range(n + 1)]


def find_group(x):
    c = []
    p = x
    while True:
        pp = group[p]
        if pp == p:
            break
        else:
            c.append(p)
            p = pp
    for i in c:
        group[i] = pp
    return pp

# find_group = lambda x: x if x == group[x] else find_group(group[x])

ans = []
not_reachable = n * (n - 1) // 2
reachable_node = []
ans.append(not_reachable)

count = not_reachable
reachable = 0
for _ in range(m - 1):
    a, b = edges.pop()
    if count > 0:
        ra = find_group(a)
        rb = find_group(b)
        if rb != ra:
            s_ra = size[ra]
            s_rb = size[rb]
            new_size = s_ra + s_rb
            reachable += num_reachable(new_size) - num_reachable(s_ra) - num_reachable(s_rb)
            size[ra] = new_size
            group[rb] = ra
        count = not_reachable - reachable
    ans.append(count)

for _ in range(len(ans)):
    print(ans.pop())