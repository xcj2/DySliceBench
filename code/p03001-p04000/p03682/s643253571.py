def main():
    import sys
    sys.setrecursionlimit(2000000)
    input = sys.stdin.readline

    class UnionFind():
        def __init__(self,n):
            self.n=n
            self.parents = [i for i in range(n+1)]
            self.size = [1]*(n+1)
        def find(self,x):
            if self.parents[x]==x:
                return x
            else:
                self.parents[x]=self.find(self.parents[x])
                return self.parents[x]
        def unite(self,x,y):
            xRoot = self.find(x)
            yRoot = self.find(y)
            if xRoot == yRoot:
                return
            if self.size[xRoot]>self.size[yRoot]:
                self.parents[yRoot] = xRoot
            else:
                self.parents[xRoot] = yRoot
                if self.size[xRoot] == self.size[yRoot]:
                    self.size[yRoot]+=1

    N = int(input())
    nodesX = []
    nodesY = []
    for i in range(1,N+1):
        x,y = map(int,input().split())
        nodesX.append((x,i))
        nodesY.append((y,i))
    nodesX.sort()
    nodesY.sort()
    edges = []
    for i in range(1,N):
        edges.append((nodesX[i][0]-nodesX[i-1][0],nodesX[i][1],nodesX[i-1][1]))
        edges.append((nodesY[i][0]-nodesY[i-1][0],nodesY[i][1],nodesY[i-1][1]))
    edges.sort()
    tree = UnionFind(N)
    cost = 0
    for w,s,t in edges:
        if tree.find(s)!= tree.find(t):
            tree.unite(s,t)
            cost += w
    print(cost)

main()