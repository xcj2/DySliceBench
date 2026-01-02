import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]

    def bfs(start):
        q = deque([start])
        visited = [-1 for _ in range(N)]
        visited[start] = 0
        prev = [set() for _ in range(N)]
        prev[start].add(-1)

        while q:
            cur = q.popleft()

            for nex in range(N):
                if cur == nex:
                    continue

                if S[cur][nex] == "0":
                    continue

                if nex in prev[cur]:
                    continue

                if visited[nex] == visited[cur] + 1:
                    prev[nex].add(cur)
                    continue

                if visited[nex] > 0:
                    return -1

                visited[nex] = visited[cur] + 1
                prev[nex].add(cur)
                q.append(nex)

        return max(visited) + 1

    # 端を決め打ちして全探索
    ans = -1
    for i in range(N):
        tmp = bfs(i)
        if ans < tmp:
            ans = tmp

    print(ans)


if __name__ == "__main__":
    main()
