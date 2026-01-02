
import collections
from functools import lru_cache
import bisect

INF = float("inf")
ZERO = 0
ONE = 1


def read():
    return input().strip()


def readInt():
    return int(input().strip())


def readList():
    return list(map(int, input().strip().split()))


def solve(N, M, arr):
    graph = collections.defaultdict(list)

    for u, v in arr:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    seen = [False] * N
    ans = 0

    for i in range(N):
        if not seen[i]:
            seen[i] = True
            q = collections.deque([i])
            componentSize = 0

            while q:
                curr = q.popleft()
                componentSize += 1

                for nei in graph[curr]:
                    if not seen[nei]:
                        seen[nei] = True
                        q.append(nei)

            ans = max(ans, componentSize)

    return ans


N, M = readList()
arr = set()

for _ in range(M):
    arr.add(tuple(sorted(readList())))

print(solve(N, M, arr))
