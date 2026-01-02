
import numpy as np
from collections import deque
import sys

def parse(inp):
    H, W = map(int, next(inp).split())
    return np.array([list(next(inp).strip()) for _ in range(H)])

dis = [0, 0, 1, -1]
djs = [1, -1, 0, 0]

def search(S, i, j, Q, R):
    H, W = S.shape
    R[i, j] = True
    Q.append((i, j))
    n0 = 0
    n1 = 0
    while Q:
        i, j = Q.popleft()
        if S[i, j] == "#":
            n1 += 1
        else:
            n0 += 1
        gen = ((i + di, j + dj) for di, dj in zip(dis, djs))
        ijs = (g for g in gen if 0 <= g[0] and g[0] < H and 0 <= g[1] and g[1] < W)
        for ni, nj in ijs:
            if not R[ni, nj] and S[ni, nj] != S[i, j]:
                R[ni, nj] = True
                Q.append((ni, nj))
    return n0 * n1


def test(S):
    i, j = 0, 0
    Q = deque()
    R = np.full(S.shape, False)
    H, W = S.shape
    n = 0
    for i in range(H):
        for j in range(W):
            if not R[i, j]:
                n += search(S, i, j, Q, R)
    return n

print(test(parse(sys.stdin)))