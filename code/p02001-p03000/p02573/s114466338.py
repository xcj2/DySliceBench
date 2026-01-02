# input here
_INPUT = """\
5 3
1 2
3 4
5 1
"""
"""
K = int(input())
H, W, K = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(N)]
p = tuple(map(int,input().split()))
"""
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]



def main():
    n, m = map(int, input().split())
    xy = [list(map(int, input().split())) for i in range(m)]

    uf = UnionFind(n)

    for i in range(len(xy)):
        uf.union(xy[i][0]-1,xy[i][1]-1)
    
    print(-(min(uf.parents)))

    
    
    

            
if __name__ == '__main__':
    import io
    import sys
    import math
    import itertools
    from collections import deque

    # sys.stdin = io.StringIO(_INPUT)
    main()