from sys import stdin
import sys
sys.setrecursionlimit(10000)


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


class DFS():
    def __init__(self, con, val):
        # 隣接リスト表現
        self.con = con
        self.val = val
        self.N = len(self.con)
        # 訪問済み?
        self.seen = [False] * self.N

    def dfs(self, v):
        self.seen[v] = True
        for next_v in self.con[v]:
            if self.seen[next_v]:
                continue
            if self.val[next_v] == 1:
                self.dfs(next_v)
        return


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    io_cnt = 0
    while True:
        try:
            w,h = list(map(int,_in[io_cnt].split(' ')))  # type:list(int)
            c_arr = []
            for i in range(h):
                _ = list(map(int,_in[io_cnt+i+1].split(' ')))  # type:list(int)
                c_arr.append(_)
            io_cnt += h+1
            # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            c_con, c_val = grid2adj(c_arr,direction=8)
            dfs = DFS(c_con,c_val)

            cnt = 0
            for v, val in enumerate(c_val):
                if val == 1:
                    if not dfs.seen[v]:
                        dfs.dfs(v)
                        cnt += 1
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            print(cnt)
        except:
            break

