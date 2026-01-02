from typing import Union, List
import sys

sys.setrecursionlimit(100000)

# 木の根を返す
def find(x: int, S: List[int]) -> int:
    if S[x] == x:
        return x
    else:
        S[x] = find(S[x], S)
        return S[x]

# xとyが同じ集合に属すかの判定
def same(x: int, y: int, S: List[int]) -> bool:
    return find(x, S) == find(y, S)

# xとyの属する集合を結合
def unite(x: int, y: int, S: List[int]) -> None:
    rx = find(x, S)
    ry = find(y, S)
    if rx == ry:
        return None
    else:
        S[rx] = ry

if __name__ == '__main__':
    [n, q] = [int(i) for i in input().split()]

    S = [i for i in range(n)]

    for i in range(q):
        [com, x, y] = [int(i) for i in input().split()]
        if com == 0:
            unite(x, y, S)
        elif com == 1:
            if same(x, y, S):
                print('1')
            else:
                print('0')
        else:
            raise ValueError('value error')

