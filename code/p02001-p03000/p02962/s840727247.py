#!/usr/bin/env python3
import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10*6)
INF = float("inf")


def z_algorithm(S):
    """Zアルゴリズム
    https://snuke.hatenablog.com/entry/2014/12/03/214243 の二番目のコード
    """
    N = len(S)
    Z = [0]*N

    c = 0
    for i in range(1, N):
        if i+Z[i-c] < c+Z[c]:
            Z[i] = Z[i-c]
        else:
            j = max(0, c+Z[c]-i)
            while i+j < N and S[j] == S[i+j]:
                j += 1
            Z[i] = j
            c = i
    Z[0] = len(S)
    return Z


def zfindall(text, pattern, separator="$"):
    """テキストからパターンと一致する部分文字列を探す。
    開始インデックスを返す
    Zアルゴリズムを利用する
    """
    N = len(pattern)
    conc = pattern+separator+text
    Z = z_algorithm(conc)
    return [i-N-1 for i in range(len(conc)) if Z[i] == N]


def solve(s: str, t: str):
    S = len(s)
    T = len(t)

    # Sの方が長くなるように
    if T > S:
        s *= int(math.ceil(T/S))

    s2 = s+s
    match = zfindall(s2, t)

    if len(match) == 0:
        print(0)
        return

    # グラフを構成し、最長パスが答え。ループがあれば-1
    # グラフは辞書で表現
    edges = {}
    rev_edges = {}
    for i, m in enumerate(match):
        if m >= S:
            continue
        edges[m] = (m+T) % S
        rev_edges[(m+T) % S] = m

    # 何度も同じ経路を確認するのを改善しうる
    maxlenpath = 1
    visitted = defaultdict(int)
    for k in edges:
        # kが含まれるパスを考える。
        # 逆向きにはったグラフを利用して、双方向の長さを求める
        if visitted[k]:
            continue
        counter = 0
        b = k
        while b in edges:
            counter += 1
            b = edges[b]
            if visitted[b]:
                print(-1)
                return
            else:
                visitted[b] = 1
        b = k
        while b in rev_edges:
            counter += 1
            b = rev_edges[b]
            if visitted[b]:
                print(-1)
                return
            else:
                visitted[b] = 1
        # print("visitted: ", visitted)
        # print("counter: ", counter)
        if maxlenpath < counter:
            maxlenpath = counter
    print(maxlenpath)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)


if __name__ == '__main__':
    main()
