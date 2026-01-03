def main():
    import sys

    def I():
        return int(sys.stdin.readline().rstrip())

    def S():
        return sys.stdin.readline().rstrip()

    N = I()
    G = [[] for i in range(N + 1)]

    for i in range(N - 1):
        a, b, c = map(int, S().split())
        G[a].append((b, c))
        G[b].append((a, c))

    Q, K = map(int, S().split())

    from collections import deque

    distance = [-1] * (N + 1)  # arrive[i] = 頂点Kからの最短距離
    distance[K] = 0

    q = deque([K])
    while q:
        a = q.pop()
        for b, c in G[a]:
            if distance[b] != -1:
                continue
            distance[b] = distance[a] + c
            q.appendleft(b)

    for i in range(Q):
        x, y = map(int, S().split())
        print(distance[x] + distance[y])

if __name__ == '__main__':
    main()