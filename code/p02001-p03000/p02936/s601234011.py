# https://atcoder.jp/contests/abc138/tasks/abc138_d

import sys
input = sys.stdin.readline
from copy import deepcopy


class Graph:
    def __init__(self, n, dictated=False, decrement=True, edge=[]):
        self.n = n
        self.dictated = dictated
        self.decrement = decrement
        self.edge = [set() for _ in range(self.n)]
        self.parent = [-1]*self.n
        self.info = [-1]*self.n
        for x, y in edge:
            self.add_edge(x,y)

    def add_edge(self, x, y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edge[x].add(y)
        if self.dictated == False:
            self.edge[y].add(x)

    def add_adjacent_list(self, i, adjacent_list):
        if self.decrement:
            self.edge[i] = set(map(lambda x:x-1, adjacent_list))
        else:
            self.edge[i] = set(adjacent_list)

    def dfs2(self, info, start, goal=-1, time=0, save=False):
        """
        :param info: 各頂点の付加情報
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: ゴール地点までの距離。存在しなければ -1
        """

        if self.decrement:
            start -= 1
            goal -= 1
        # if not save:
        #     self.parent = [-1] * self.n
        #
        edge2 = deepcopy(self.edge)


        p, t = start, time
        self.parent[p] = -2
        while True:
            if edge2[p]:
                q = edge2[p].pop()
                if q == self.parent[p] and not self.dictated:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if self.parent[q] != -1:
                    """ サイクルで同一点を訪れた時の処理 """
                    """"""""""""""""""""
                    continue
                if q == goal:
                    """ ゴール時の処理"""
                    # return t + 1
                    """"""""""""""""""""
                    continue
                """ p から q への引継ぎ"""
                info[q] += info[p]
                """"""""""""""""""""
                self.parent[q] = p
                p, t = q, t + 1
            else:
                """ 探索完了時の処理 """
                """"""""""""""""""""
                if p == start and t == time:
                    break
                p, t = self.parent[p], t-1
                """ 二度目に訪問時の処理 """

                """"""""""""""""""""
        return info


######################################################################################################

N, Q = map(int, input().split())  # N:頂点数, Q: クエリの数
M = N-1

graph = Graph(N, dictated=False)

for _ in range(M):
    x, y = map(int, input().split())
    graph.add_edge(x,y)

info = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    info[p - 1] += x

print(*graph.dfs2(info, start=1))
