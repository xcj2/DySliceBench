
import numpy as np


from functools import *
import sys
sys.setrecursionlimit(100000)


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())


mod = 10**9+7


class UnionFind:
    def __init__(self, size):
        # -nが木のroot
        # 親ノードの位置を格納
        self.table = [-1 for i in range(size)]

    def _find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def find(self, x):
        if self.table[x] < 0:
            return x
        self.table[x] = self.find(self.table[x])
        return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] >= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    def get_ntree(self):
        res = 0
        for c in self.table:
            if c < 0:
                res += 1
        return res

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_nclass(self):
        done = []
        for x in range(len(self.table)):
            if x in done:
                continue
            while self.table[x] >= 0:
                done.append(x)
                x = self.table[x]

    def get_nodenum(self):
        res = []
        for t in self.table:
            if t < 0:
                res.append(-t)

        return res


def ij_to_n(i, j, W):
    return i*W+j


def n_to_ij(n, W):
    return (n//W, n % W)


if __name__ == '__main__':

    N, M, K = acinput()

    uf = UnionFind(N)
    A=[[]for i in range(N)]
    for i in range(M):
        tmp = acinput()
        uf.union(tmp[0]-1, tmp[1]-1)
        A[tmp[0]-1].append(tmp[1]-1)
        A[tmp[1]-1].append(tmp[0]-1)


    block=[[]for i in range(N)]
    for i in range(K):
        tmp = acinput()
        block[tmp[0]-1].append(tmp[1]-1)
        block[tmp[1]-1].append(tmp[0]-1)

    nt = uf.get_ntree()
    res=[]
    for i in range(N):
        nblock = 0
        for sb in block[i]:
            if uf.is_same(sb,i):
                nblock += 1

        nn =(-uf.table[uf.find(i)])

        nn-=1
        
        #print(uf.find(i),nn, A[i], nblock)
        tmp = nn-(len(A[i]))-nblock
        res.append(tmp)

    print(" ".join(map(str,res)))
