def main():
    from collections import deque
    H, W = (int(i) for i in input().split())
    Ch, Cw = (int(i)-1 for i in input().split())
    Dh, Dw = (int(i)-1 for i in input().split())
    A = [input() for i in range(H)]
    V = [-1]*((H-1)*W + W)  # 頂点i

    def bfs_2d(sy, sx, v):
        que = deque()
        V[sy*W+sx] = v
        que.append(sy*W+sx)
        d = ((0, -1), (0, 1), (-1, 0), (1, 0))
        while que:
            u = que.popleft()
            uh, uw = u//W, u % W
            for dy, dx in d:
                next_h = uh + dy
                next_w = uw + dx
                if not(0 <= next_h < H and 0 <= next_w < W):
                    continue
                if V[next_h*W+next_w] != -1:
                    continue
                if A[next_h][next_w] == '#':
                    continue
                V[next_h*W+next_w] = v
                que.append(next_h*W + next_w)

    vertex = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] == "#" or V[h*W+w] != -1:
                continue
            bfs_2d(h, w, vertex)
            vertex += 1

    G = [[] for _ in range(vertex)]
    used = [set() for _ in range(vertex)]
    for h in range(H):
        for w in range(W):
            if A[h][w] == "#":
                continue
            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    if h + dh < 0 or H <= h + dh or w + dw < 0 or W <= w + dw:
                        continue
                    if A[h+dh][w+dw] == "#":
                        continue
                    if V[h*W+w] == V[(h+dh)*W + w+dw]:
                        continue
                    if V[(h+dh)*W + w+dw] in used[V[h*W+w]]:
                        continue
                    G[V[h*W+w]].append(V[(h+dh)*W + w+dw])
                    used[V[h*W+w]].add(V[(h+dh)*W + w+dw])

    # print(V)
    # for i in range(vertex):
    #     print(G[i])

    def bfs(s, g, N):
        que = deque([s])
        dist = [-1]*N
        dist[s] = 0
        while que:
            v = que.popleft()
            for i in G[v]:
                if dist[i] != -1:
                    continue
                que.append(i)
                dist[i] = dist[v] + 1
        return dist[g]

    s = V[Ch*W+Cw]
    g = V[Dh*W+Dw]
    ans = bfs(s, g, vertex)
    print(ans)


if __name__ == '__main__':
    main()
