import sys, collections

def dfs(i, c, col, edge):
    col[i] = c
    for next_node in edge[i]:
        if col[next_node] == c: return False
        if col[next_node] == 0 and dfs(next_node, -c, col, edge) == False: return False

    return True

def longest(i, edge, N):
    q = collections.deque()
    q.append((i, 1))
    dist = dict()
    ans = 1
    for j in range(N): dist[j] = -1
    flag = True
    while q:
        nn, nd = q.popleft()
        if dist[nn] == -1:
            ans = max(nd, ans)
            dist[nn] = nd
            for next_node in edge[nn]:
                if dist[next_node] == -1: q.append((next_node, nd + 1))
                elif abs(dist[next_node] - nd) != 1: flag = False
        elif dist[nn] != nd:
            ans = -1
            break
    #print(i, dist)
    return (ans if flag else -1)

def solve():
    N = int(input())
    edge = dict()
    col = dict()
    for i in range(N): 
        edge[i] = set()
        col[i] = 0
        s = input()
        for j in range(N):
            if s[j] == "1": edge[i] |= {j}

    is_bipartite = dfs(0, 1, col, edge)
    if not is_bipartite: print(-1)
    else:
        ans = -1
        for i in range(N):
            ans = max(ans, longest(i, edge, N))
        print(ans)

    return 0

if __name__ == "__main__":
    solve()
