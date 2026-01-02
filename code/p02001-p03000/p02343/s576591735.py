# import bisect
# from collections import Counter, deque
# import copy
# from fractions import gcd
# from functools import reduce
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline

def resolve():
    class UnionFind(object):
        def __init__(self, n=1):
            # 木の親要素を管理するリストparをつくります。
            # par[x] == xの場合には、そのノードが根であることを示します。
            # 初期状態では一切グループ化されていないので、すべてのノードが根になりますね。
            self.par = [i for i in range(n)]
            # 木の高さを持っておき、あとで低い方を高い方につなげる。初期状態は0
            self.rank = [0 for _ in range(n)]
            self.size = [1 for _ in range(n)]

        def find(self, x):
            """
            x が属するグループを探索：
            ある２つの要素が属する木の根が同じかどうかをチェックすればよい。
            つまり、親の親の親の・・・と根にたどり着くまで走査すればよい。
            再帰。
            """
            # 根ならその番号を返す
            if self.par[x] == x:
                return x
            # 根でないなら、親の要素で再検索
            else:
                # 一度見た値については根に直接繋いで経路圧縮
                # 親を書き換えるということ
                self.par[x] = self.find(self.par[x])
                return self.par[x]

        def union(self, x, y):
            """
            x と y のグループを結合
            """
            # 根を探す
            x = self.find(x)
            y = self.find(y)
            # 小さい木に結合して経路圧縮
            if x != y:
                if self.rank[x] < self.rank[y]:
                    x, y = y, x
                # 同じ長さの場合rankが1増える
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
                # 低い方の木の根を高い方の根とする
                self.par[y] = x
                self.size[x] += self.size[y]

        def is_same(self, x, y):
            """
            x と y が同じグループか否か
            """
            return self.find(x) == self.find(y)

        def get_size(self, x):
            """
            x が属するグループの要素数
            """
            x = self.find(x)
            return self.size[x]

    N, Q = map(int, input().split())
    uf = UnionFind(N)  # ノード数Nでクラス継承

    for i in range(Q):
        # A,Bはノード
        P, A, B = map(int, input().split())
        if P == 0:
            # 連結クエリ union
            uf.union(A, B)
        else:
            # 判定クエリ find
            if uf.is_same(A, B):
                print(1)
            else:
                print(0)


resolve()
