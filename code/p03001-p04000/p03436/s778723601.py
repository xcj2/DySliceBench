from collections import deque
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    H, W = read_ints()
    S = []
    for _ in range(H):
        S.append(input().strip())
    Q = deque([(0, 0, 0)])
    INF = 10**9
    costs = [[INF]*W for _ in range(H)]
    costs[0][0] = 0
    while Q:
        i, j, cost = Q.popleft()
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < H and 0 <= y < W and costs[x][y] == INF and S[x][y] == '.':
                costs[x][y] = cost+1
                Q.append((x, y, cost+1))
    if costs[H-1][W-1] == INF:
        return -1
    whites = sum(1 for row in S for c in row if c == '.')
    return whites-(costs[H-1][W-1]+1)


if __name__ == '__main__':
    print(solve())
