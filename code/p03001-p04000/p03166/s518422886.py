import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    V, E = map(int, input().split())
    is_visited = [False] * V
    indeg = [0] * V  # 流入量
    # 隣接リスト
    G = defaultdict(lambda: [])

    for i in range(E):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        G[s].append(t)
        indeg[t] += 1

    # print(G, indeg, is_visited)
    out = []
    dp = [0] * V

    def bfs(s):
        q = deque()
        q.append(s)
        is_visited[s] = True
        while q:
            u = q.popleft()
            out.append(u)
            # print(u, out)
            for v in G[u]:
                indeg[v] -= 1
                # dp[v] = max(dp[v], dp[u] + 1)
                if indeg[v] == 0 and (not is_visited[v]):
                    q.append(v)
                    is_visited[v] = True

    def topological():
        for u in range(V):
            if indeg[u] == 0 and (not is_visited[u]):
                bfs(u)

        # print(max(dp))

    topological()

    for i in out:
        for dest in G[i]:
            dp[dest] = max(dp[dest], dp[i] + 1)

    print(max(dp))


if __name__ == "__main__":
    main()
