
def read_data():
    N = int(input())
    Es = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        Es[a - 1].append(b - 1)
        Es[b - 1].append(a - 1)
    return N, Es

def solve(N, Es):
    if N == 2:
        return "Snuke"
    path = find_path(N, 0, N - 1, Es)
    len_path = len(path)
    a = (len_path - 1)// 2
    b = a + 1
    p1 = path[a]
    p2 = path[b]
    e1 = count_edges(N, p1, p2, Es)
    e2 = N - e1
    if e1 > e2:
        return "Fennec"
    else:
        return "Snuke"

def find_path(N, s, g, Es):
    stack = [(s, 0)]
    path = []
    visited = [False] * N
    visited[s] = True
    while True:
        v, d = stack[-1]
        if (path and path[-1][0] == v):
            stack.pop()
            path.pop()
            continue
        if (path and path[-1][1] >= d):
            path.pop()
        path.append((v, d))
        for u in Es[v]:
            if visited[u]:
                continue
            stack.append((u, d + 1))
            visited[u] = True;
            if u == g:
                path = [p for p, depth in path] + [g]
                return path

def count_edges(N, p1, p2, Es):
    stack = [p1]
    visited = [False] * N
    visited[p1] = True
    visited[p2] = True
    count = 0
    while stack:
        v = stack.pop()
        count += 1
        for u in Es[v]:
            if visited[u]:
                continue
            stack.append(u)
            visited[u] = True
    return count


N, Es = read_data()
print(solve(N, Es))
    