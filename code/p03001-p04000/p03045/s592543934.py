
import numpy as np
import sys
sys.setrecursionlimit(100000)


class UnionFind:
    def __init__(self, size):
        # -nが木のroot
        #親ノードの位置を格納
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



def acinput():
    return list(map(int, input().split(" ")))



directions=np.array([[1,0],[0,1],[-1,0],[0,-1]])
directions = list(map(np.array, directions))

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact



def serch(x, count):
    #print("top", x, count)
            

    for d in directions:
        nx = d+x
        #print(nx)
        if np.all(0 <= nx) and np.all(nx < (H, W)):
            if field[nx[0]][nx[1]] == "E":
                count += 1 
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)  
                continue
            if field[nx[0]][nx[1]] == "#":
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)    
                 
    return count


N,M=acinput()

uf = UnionFind(N)

for i in range(M):
    tmp = acinput()
    uf.union(tmp[0]-1,tmp[1]-1)


print(uf.get_ntree())

