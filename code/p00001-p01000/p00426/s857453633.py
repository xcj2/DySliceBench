from sys import stdin
from collections import deque


def l2t(g):
    return tuple(map(tuple,g))




class BFS():
    def __init__(self, graph, m, n):
        # 盤面
        self.graph = graph
        self.m = m
        self.n = n
        # 始点からの距離
        self.dist = {}
        # キュー
        self.que = deque()

        self.eg_arr = [[[i for i in range(1,self.n+1)],[],[]],
                       [[],[],[i for i in range(1,self.n+1)]]]

    def list2num(self,g):
        str_ = ''
        for i in range(self.n):
            if i+1 in g[0]:
                str_ += '0'
            elif i+1 in g[1]:
                str_ += '1'
            else:
                str_ += '2'
        return str_

    def bfs(self):
        self.graph = self.list2num(self.graph)
        self.eg_arr[0] = self.list2num(self.eg_arr[0])
        self.eg_arr[1] = self.list2num(self.eg_arr[1])

        # 初期条件
        self.dist[self.graph] = 0
        self.que.append(self.graph)

        if self.graph in self.eg_arr:
            return 0

        while self.que:
            g = self.que.popleft()
            if self.dist[g] > self.m: continue

            ng_arr = []
            ind0 = g.rfind('0')
            ind1 = g.rfind('1')
            ind2 = g.rfind('2')
            if ind0 >= 0:
                if (ind1 >= 0 and ind1<ind0) or ind1 < 0:
                    ng = g[:ind0]+'1'+g[ind0+1:]
                    ng_arr.append(ng)
            if ind1 >= 0:
                if (ind0 >= 0 and ind0<ind1) or ind0 < 0:
                    ng = g[:ind1]+'0'+g[ind1+1:]
                    ng_arr.append(ng)
                if (ind2 >= 0 and ind2<ind1) or ind2 < 0:
                    ng = g[:ind1]+'2'+g[ind1+1:]
                    ng_arr.append(ng)
            if ind2 >= 0:
                if (ind1 >= 0 and ind1<ind2) or ind1 < 0:
                    ng = g[:ind2]+'1'+g[ind2+1:]
                    ng_arr.append(ng)

            for ng in ng_arr:
                if ng in self.dist.keys(): continue
                self.dist[ng] = self.dist[g] + 1
                self.que.append(ng)
                if ng in self.eg_arr:
                    return self.dist[ng]
        else:
            return -1


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    io_cnt = 0
    while True:
        try:
            n, m = list(map(int,_in[io_cnt].split(' ')))  # type:list(int)
            graph = []
            for i in range(3):
                _ = list(map(int,_in[io_cnt+i+1].split(' ')))  # type:list(int)
                if _[0] == 0:
                    graph.append([])
                else:
                    graph.append(_[1:])
            io_cnt += 4
            # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            bfs = BFS(graph,m,n)
            cnt = bfs.bfs()
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            print(cnt)
        except:
            break


if __name__ == "__main__":
    main()

