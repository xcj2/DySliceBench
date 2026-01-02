class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0]*size
    
    def find(self, x):
        stack = []
        parent = self.parent
        while parent[x] != x:
            stack.append(x)
            x = parent[x]
        for y in stack:
            parent[y] = x
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif xr != yr:
            self.parent[yr] = xr
            self.rank[xr] += 1


max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

def solve(points):
    N = len(points)
    XI = [0]*N
    YI = [0]*N

    for i,(x,y) in enumerate(points):
        XI[x] = i
        YI[y] = i

    ds = DisjointSet(N)

    offset = N
    y_max_connected = -1
    rep = -1
    for i in YI:
        x0,y0 = points[i]
        if x0 >= offset:
            continue

        t = y0
        for j in XI[x0+1:offset]:
            x,y = points[j]
            if y >= y0:
                ds.union(i,j)
                t = max2(t, y)
        offset = x0

        if y_max_connected >= y0:
            ds.union(rep, i)
            y_max_connected = max2(y_max_connected,t)
        else:
            y_max_connected = t
            rep = i
        # print(y0, y_max_connected)


    cnt = [0]*N
    for i in range(N):
        cnt[ds.find(i)] += 1

    return [cnt[ds.find(i)] for i in range(N)]

# import numpy as np
# from itertools import combinations
# def naive(points):
#     N = len(points)
#     grid = np.zeros((N,N), dtype=bool)
#     for x,y in points:
#         grid[x,y] = True
#     ds = DisjointSet(N)
#     for i,j in combinations(range(N),2):
#         x0,y0 = points[i]
#         x1,y1 = points[j]
#         if np.any(grid[max(x0,x1):,max(y0,y1):]) or np.any(grid[:min(x0,x1),:min(y0,y1)]):
#             ds.union(i,j)

#     cnt = [0]*N
#     for i in range(N):
#         cnt[ds.find(i)] += 1

#     return [cnt[ds.find(i)] for i in range(N)]

# from random import shuffle

if __name__ == '__main__':
    N = int(readline())
    m = map(lambda x: int(x)-1, read().split())

    points = tuple(zip(m,m))

    print(*solve(points), sep='\n')

    # N = 12

    # X = list(range(N))
    # for k in range(100000):
    #     if k % 10000:
    #         print(k)
    #     Y = list(range(N))
    #     shuffle(Y)
    #     points = [(x,y) for x,y in zip(X,Y)]
    #     r1,r2 = solve(points),naive(points)
    #     if r1 != r2:
    #         print(Y)
    #         print(r1)
    #         print(r2)
    #         break
