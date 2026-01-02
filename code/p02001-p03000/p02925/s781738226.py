import sys
from collections import defaultdict


sys.setrecursionlimit(10**6)


def pair2index(i, j, N):
    return N * i + j


def main():
    N = int(input())
    adj = defaultdict(list)
    for i in range(N):
        A = list(map(lambda x: int(x) - 1, input().split(' ')))
        for j in range(1, N - 1):
            a = A[j - 1]
            from_index = pair2index(min(i, a), max(i, a), N)
            a = A[j]
            to_index = pair2index(min(i, a), max(i, a), N)
            adj[from_index].append(to_index)

    temp_visited = [0 for _ in range(N**2)]
    max_depth = [0 for _ in range(N**2)]

    def dfs(n):
        if temp_visited[n] == 1:
            # 閉路あり
            max_depth[n] = -1
            return -1
        elif max_depth[n] != 0:
            return max_depth[n]
        else:   # max_depth[n] == 0 (未探索)
            temp_visited[n] = 1
            max_d = 0
            for next_n in adj[n]:
                d = dfs(next_n)
                if d == -1:
                    return d
                max_d = max(max_d, d)
            temp_visited[n] = 0
            max_depth[n] = max_d + 1
            return max_d + 1

    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            node = pair2index(i, j, N)
            depth = dfs(node)
            if depth == -1:
                print(-1)
                return
            ans = max(ans, depth)
    print(ans)


if __name__ == '__main__':
    main()