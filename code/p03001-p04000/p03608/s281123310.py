import math
from typing import List, Counter, Tuple
from collections import Counter
from itertools import permutations


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> int:
    N, M, R = read_ints()
    r = [a-1 for a in read_ints()]
    inf = 10**10
    D = [
        [inf for _ in range(N)] for _ in range(N)
    ]
    for i in range(N):
        D[i][i] = 0
    for _ in range(M):
        a, b, c = read_ints()
        D[a-1][b-1] = D[b-1][a-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    min_cost: int = inf
    for path in permutations(r):
        cost: int = 0
        for i in range(1, len(path)):
            cost += D[path[i-1]][path[i]]
        min_cost = min(min_cost, cost)
    return min_cost


if __name__ == '__main__':
    print(solve())
