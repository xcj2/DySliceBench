def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    inf = 1 << 60

    N, M, P = map(int, input().split())

    to = tuple(set() for _ in range(N))
    ot = tuple(set() for _ in range(N))
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        to[a].add((b, -(c - P)))  # to,coin(負辺)
        ot[b].add((a, -(c - P)))  # to,coin(負辺)

    def reach(s, g, result):
        dq = deque()
        dq.append(s)
        while dq:
            v = dq.popleft()
            for u, _ in g[v]:
                if result[u]: continue
                result[u] = 1
                dq.append(u)

    reachable_from_N = [0] * N
    reachable_from_N[N - 1] = 1
    reach(N - 1, ot, reachable_from_N)

    reachable_from_1 = [0] * N
    reachable_from_1[0] = 1
    reach(0, to, reachable_from_1)

    unreachable = tuple(1 ^ (rn & r1) for rn, r1 in zip(reachable_from_N, reachable_from_1))

    def bellman_ford(dist):
        for _ in range(N):
            not_updated = True
            for v in range(N):
                for u, c in to[v]:
                    if unreachable[u]: continue
                    if (dist[v] == inf) or (dist[v] + c >= dist[u]): continue
                    dist[u] = dist[v] + c
                    not_updated = False
            if not_updated: return False

        for v in range(N):  # 負閉路検知
            for u, c in to[v]:
                if unreachable[u]: continue
                if (dist[v] == inf) or (dist[v] + c >= dist[u]): continue
                return True
        return False

    dist = [inf] * N
    dist[0] = 0
    cond = bellman_ford(dist=dist)

    if cond:
        print(-1)
    else:
        print(max(0, -dist[N - 1]))


if __name__ == '__main__':
    main()
