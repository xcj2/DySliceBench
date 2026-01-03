# 6199094

import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self,n):
        self.parent = [-1 for _ in range(n)]

    def size(self,x):
        return -self.parent[self.find(x)]

    def find(self,x):
        if(self.parent[x]<0):
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]

    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return False
        if(self.size(x)<self.size(y)):
            self.parent[y]+=self.parent[x]
            self.parent[x]=y
        else:
            self.parent[x]+=self.parent[y]
            self.parent[y]=x
        return True

    def same(self,x,y):
        return self.find(x)==self.find(y)

def main():
    N = int(input())
    xli = []
    yli = []
    x_app = xli.append
    y_app = yli.append


    for i in range(N):
        x,y = (int(x) for x in input().split())
        x_app([x-1,i])
        y_app([y-1,i])
    xli.sort()
    yli.sort()

    edges = []
    edges_app = edges.append
    for i in range(N-1):
        edges_app((xli[i][1],xli[i+1][1],xli[i+1][0]-xli[i][0]))
        edges_app((yli[i][1],yli[i+1][1],yli[i+1][0]-yli[i][0]))


    edges.sort(key=lambda edge: edge[2])
    uf = UnionFind(N)
    weight = 0

    for edge in edges:
        if not uf.same(edge[0], edge[1]):
            uf.unite(edge[0], edge[1])
            weight+=edge[2]
    print(weight)

if __name__ == '__main__':
    main()
