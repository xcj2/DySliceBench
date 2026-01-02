#####################################################################################################
##### 深さ優先探索 幅優先探索　（グラフ）
#####################################################################################################

'''

キューに頂点を入れる回数は各々高々１回のみ。
各辺を使う回数は高々一回のみ（辺を戻るような探索は枝切りされている）
結果として、計算量はO(N + M)

'''

import sys
sys.setrecursionlimit(10 ** 8)
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

    def cycle_detector(self, start, time=0, save=False):
        """
        :param p: スタート地点
        :param save: True = 前回の探索結果を保持する
        :return: 各点までの距離と何番目に発見したかを返す
        """

        edge2 = deepcopy(self.edge)

        if self.decrement:
            start -= 1
        if not save:
            self.parent = [-1] * self.n

        p, t = start, time
        self.parent[p] = -2
        cycle_end = False
        cycle_time = 0
        cycle = []
        while True:
            if edge2[p]:
                q = edge2[p].pop()
                if q == self.parent[p] and not self.dictated:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if self.parent[q] != -1:
                    """ サイクルで同一点を訪れた時の処理 """
                    if not cycle:
                        if q == p:
                            """ 自己ループの時 """
                            cycle.append(q + self.decrement)
                            cycle_end = True
                        else:
                            cycle.append(q + self.decrement)
                            cycle.append(p + self.decrement)
                            cycle_time = t

                    """"""""""""""""""""
                    continue
                self.parent[q] = p
                p, t = q, t + 1
            else:
                """ 探索完了時の処理 """
                """"""""""""""""""""
                if p == start and t == time:
                    break
                p, t = self.parent[p], t-1
                """ 二度目に訪問時の処理 """
                if cycle and t == cycle_time - 1 and not cycle_end:
                    if cycle[0] == p + self.decrement:
                        cycle_end = True
                        continue
                    cycle.append(p + self.decrement)
                    cycle_time = t

                """"""""""""""""""""
        cycle = list(reversed(cycle))
        return [cycle[-1]] + cycle[:-1]

    def tree_counter(self, detail=False):
        """
        :param detail: True = サイクルのリストを返す
        :return: 木（閉路を含まない）の個数を返す
        """
        self.parent = [-1] * self.n

        connection_number = 0
        cycle_list = []

        for p in range(self.n):
            if self.parent[p] == -1:
                connection_number += 1
                cycle = self.cycle_detector(p + self.decrement, save=True)
                if cycle:
                    cycle_list.append(cycle)
        if not detail:
            return connection_number - len(cycle_list)
        else:
            return cycle_list

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        if self.dictated:
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        for x in range(self.n):
            for y in self.edge[x]:
                G.add_edge(x + self.decrement, y + self.decrement)

        nx.draw_networkx(G)
        plt.show()

##################################################################


N, K = map(int, input().split())
A = list(map(int, input().split()))

M = N
graph = Graph(N,dictated=True)
for i in range(1,M+1):
    x = i
    y = A[i-1]
    graph.add_edge(x, y)

p = 0
cnt = 0
if K <= N:
    while cnt + 1 <= K:
        p = A[p] - 1
        cnt += 1
    res = p + 1
else:
    cycle = list(graph.cycle_detector(1))
    len_cycle = len(cycle)
    p = 0
    cnt = 0
    res = 0
    while p != cycle[0] - 1:
        p = A[p] - 1
        cnt += 1
    k = (K - cnt) % len_cycle
    res = cycle[k]
print(res)



