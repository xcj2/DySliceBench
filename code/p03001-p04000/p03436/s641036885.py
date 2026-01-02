from sys import stdin
from collections import deque
from collections import Counter


def grid2adj(arr_grid,direction=4):
    def cand(i,j,direction):
        if direction == 4:
            return [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        elif direction == 8:
            return [[i-1,j],[i+1,j],[i,j-1],[i,j+1],
                    [i-1,j-1],[i-1,j+1],[i+1,j-1],[i+1,j+1]]
        else:
            print('Error')
    
    M,N = len(arr_grid),len(arr_grid[0])
    arr_con = [[] for i in range(M*N)]
    for i in range(M):
        for j in range(N):
            v = i*N+j
            for _cand in cand(i,j,direction):
                if 0<=_cand[0]<M and 0<=_cand[1]<N:
                    next_v = _cand[0]*N+_cand[1]
                    arr_con[v].append(next_v)
    arr_val = sum(arr_grid,[])

    return arr_con, arr_val


class BFS():
    def __init__(self, con, val=None):
        # 隣接リスト表現
        self.con = con
        self.val = val
        self.N = len(self.con)
        # 始点からの距離
        self.dist = [-1]*self.N
        self.que = deque()

    def bfs(self, start_v):
        # 初期条件(0-indexed)
        self.dist[start_v] = 0
        self.que.append(start_v)

        while len(self.que)>0:
            v = self.que.popleft()
            for next_v in self.con[v]:
                if self.dist[next_v] != -1:
                    continue
                if self.val[next_v] == '#':
                    continue
                self.dist[next_v] = self.dist[v] + 1
                self.que.append(next_v)


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    H, W = list(map(int,_in[0].split(' ')))  # type:list(int)
    graph = []
    for i in range(H):
        _ = list(_in[i+1])  # type:list(str)
        graph.append(_)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    g_con, g_val = grid2adj(graph)
    bfs = BFS(g_con,g_val)

    cnt = 0
    bfs.bfs(0)
    if bfs.dist[-1] == -1:
        cnt = -1
    else:
        cnt = H*W-bfs.val.count('#')-(bfs.dist[-1]+1)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
