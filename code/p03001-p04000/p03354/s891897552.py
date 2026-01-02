import sys
from copy import copy

sys.setrecursionlimit(10**5)

# 木の根を返す
def find(x, S):
    if S[x] == x:
        return x
    else:
        S[x] = find(S[x], S)
        return S[x]

# xとyが同じ集合に属すかの判定
def same(x, y, S):
    return find(x, S) == find(y, S)

# xとyの属する集合を結合
def unite(x, y, S):
    rx = find(x, S)
    ry = find(y, S)
    if rx == ry:
        return None
    else:
        S[rx] = ry

if __name__ == '__main__':
    [N, M] = [int(i) for i in input().split()]

    S = [int(i) for i in range(N+1)]
    p = [0] + [int(num) for num in input().split()]

    for i in range(M):
        [x, y] = [int(i) for i in input().split()]
        unite(x, y, S)

    score = 0
    for i in range(1, N+1):
        if same(i, p[i], S):
            score += 1
    print(score)
