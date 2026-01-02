# from typing import List
import sys

sys.setrecursionlimit(100000)

# 木の根を返す
# def find(x: int, S: List[int]) -> int:
def find(x, S):
    if S[x] == x:
        return x
    else:
        S[x] = find(S[x], S)
        return S[x]

# xとyが同じ集合に属すかの判定
# def same(x: int, y: int, S: List[int]) -> bool:
def same(x, y, S):
    return find(x, S) == find(y, S)

# xとyの属する集合を結合
# def unite(x: int, y: int, S: List[int]) -> None:
def unite(x, y, S):
    rx = find(x, S)
    ry = find(y, S)
    if rx == ry:
        return None
    else:
        S[rx] = ry

if __name__ == '__main__':
    [V, E] = [int(i) for i in input().split()]

    S = [i for i in range(V)]
    edges = []

    ans = 0

    for i in range(E):
        edges.append([int(i) for i in input().split()])

    for s, t, w in sorted(edges, key=lambda x: x[2]):
        if same(s, t, S):
            continue
        else:
            unite(s, t, S)
            ans += w


    print(ans)



