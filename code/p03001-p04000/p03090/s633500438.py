
def read_tokens():
    return input().strip().split(' ')

def read_ints():
    return [int(token) for token in read_tokens()]

def connected(edges):
    n = len(edges)
    vis = [False] * n
    def dfs(u):
        if vis[u]:
            return
        vis[u] = True
        for v in edges[u]:
            dfs(v)
    dfs(0)
    return all(vis)

def good(edges):
    n = len(edges)
    s = []
    for i in range(n):
        s.append(sum(edges[i]) + len(edges[i]))
    return min(s) == max(s)

# n, = read_ints()
# m = n * (n - 1) // 2
# for mask in range(1, 2**m):
#     edges = [[] for _ in range(n)]
#     mm = mask
#     for u in range(n):
#         for v in range(u + 1, n):
#             if mm % 2 > 0:
#                 edges[u].append(v)
#                 edges[v].append(u)
#             mm = mm // 2
#     # print(mask, edges)
#     if connected(edges) and good(edges):
#         print(edges)

def out(edges):
    print(sum(len(a) for a in edges) // 2)
    for idx, a in enumerate(edges):
        for v in a:
            if idx < v:
                print(idx+1, v+1)


def even(n):
    edges = [[] for _ in range(n)]
    s = (n + 1) * (n - 2) // 2
    sums = [s] * n
    for i in reversed(range(n)):
        # print(i, sums, edges)
        for j in reversed(range(i)):
            # if j + 1 <= sums[i] and i + 1 <= sums[j]:
            if i + j != n - 1:
                sums[i] -= j + 1
                sums[j] -= i + 1
                edges[i].append(j)
                edges[j].append(i)
    assert(max(sums) == 0 and min(sums) == 0)
    return edges

def odd(n):
    edges = [[] for _ in range(n)]
    s = n * (n - 1) // 2
    sums = [s] * n
    for i in reversed(range(n)):
        # print(i, sums, edges)
        for j in reversed(range(i)):
            # if j + 1 <= sums[i] and i + 1 <= sums[j]:
            if i + j != n - 2:
                sums[i] -= j + 1
                sums[j] -= i + 1
                edges[i].append(j)
                edges[j].append(i)
    assert(max(sums) == 0 and min(sums) == 0)
    return edges

n, = read_ints()
if n % 2 == 0:
    out(even(n))
else:
    out(odd(n))