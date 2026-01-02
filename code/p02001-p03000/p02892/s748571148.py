# AGC039B - Graph Partition
def is_bipartite() -> bool:
    stack = [(1, 1)]
    color = [-1] * (N + 1)
    color[1] = 1
    while stack:
        v, cur_color = stack.pop()
        next_color = cur_color ^ 1
        for u in E[v]:
            if color[u] == cur_color:
                return False
            if color[u] == -1:
                color[u] = next_color
                stack.append((u, next_color))
    return True


def bfs(start) -> int:
    que = [start]
    dist = [-1] * (N + 1)  # dist[i] := distance from V_start to V_i
    dist[start] = 0
    while que:
        v = que.pop(0)
        cur = dist[v]
        for u in E[v]:
            if dist[u] == -1:
                dist[u] = cur + 1
                que.append(u)
    return max(dist)


def main():
    # if bipartite graph -> diameter of the graph + 1
    global N, E
    N, *S = open(0).read().split()
    N = int(N)
    E = [0] + [[i for i, flg in enumerate(s, 1) if flg == "1"] for s in S]
    if is_bipartite():
        ans = max(bfs(i) for i in range(1, N + 1)) + 1
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()