from sys import stdin
from collections import deque


class BFS():
    def __init__(self, grid_graph):
        # grid表現
        self.graph = grid_graph
        self.H = len(self.graph)
        self.W = len(self.graph[0])
        # 始点からの距離
        self.dist = [[-1]*self.W for i in range(self.H)]
        # キュー
        self.que = deque()

    def bfs(self, sv_arr):
        dx = [ 1, 0,-1, 0]
        dy = [ 0, 1, 0,-1]

        # 初期条件(0-indexed)
        for sv in sv_arr:
            self.dist[sv[0]][sv[1]] = 0
            self.que.append(sv)

        while self.que:
            v = self.que.popleft()
            for _dx, _dy in zip(dx,dy):
                nv = [v[0]+_dx,v[1]+_dy]
                if not 0<=nv[0]<self.H: continue 
                if not 0<=nv[1]<self.W: continue
                if self.dist[nv[0]][nv[1]] != -1: continue
                self.dist[nv[0]][nv[1]] = self.dist[v[0]][v[1]] + 1
                self.que.append(nv)


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    H, W = list(map(int,_in[0].split(' ')))  # type:list(int)
    graph = []
    for i in range(H):
        _ = list(_in[i+1])  # type:list(str)
        graph.append(_)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    bfs = BFS(graph)

    sv_arr = []
    for i in range(H):
        for j in range(W):
            if bfs.graph[i][j] == '#':
                sv_arr.append([i,j])

    bfs.bfs(sv_arr)
    cnt = max(max(_) for _ in bfs.dist)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)


if __name__ == "__main__":
    main()
