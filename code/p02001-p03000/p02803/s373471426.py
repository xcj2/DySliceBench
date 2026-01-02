import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    H, W = read_ints()
    last_S = ''
    INF = 10**9+1
    dist = [
        [INF for _ in range(H*W)] for _ in range(H*W)
    ]
    for i in range(H*W):
        dist[i][i] = 0
    for i in range(H):
        S = input().strip()
        for j in range(W):
            if S[j] == '#':
                continue
            top = (i-1)*W+j
            left = i*W+j-1
            current = i*W+j
            if j > 0 and S[j-1] == '.':
                dist[left][current] = dist[current][left] = 1
            if i > 0 and last_S[j] == '.':
                dist[top][current] = dist[current][top] = 1
        last_S = S
    for k in range(H*W):
        for i in range(H*W):
            for j in range(H*W):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return max(cell for row in dist for cell in row if cell != INF)


if __name__ == '__main__':
    print(solve())
