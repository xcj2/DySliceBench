#!/usr/bin/env python3
from collections import deque
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    G = [[] for _ in range(N)]
    for i, (ai, bi) in enumerate(zip(a, b)):
        ai -= 1
        bi -= 1
        G[ai].append((i, bi))
        G[bi].append((i, ai))

    ans = 0
    for k in range(M):
        q = deque()
        visited = {0}
        q.append(0)
        while q:
            s = q.popleft()
            for i, t in G[s]:
                if i == k:
                    continue
                if t in visited:
                    continue
                visited.add(t)
                q.append(t)

        if len(visited) < N:
            ans += 1

    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == '__main__':
    main()
