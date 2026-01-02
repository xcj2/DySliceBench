import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
class UnionFind:
    #ノード番号は0-indexである
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.length = [1 for _ in range(n)] 
        self.numberOfElements = n
    #UnionFindを初期化する関数
    def makeSet(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.length = [1 for _ in range(n)]
        self.numberOfElements = n

    #ノードxのrootを探して返す関数
    def findRoot(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.findRoot(self.parents[x])
            return self.parents[x]

    #ノードxとノードyを連結する関数
    def uniteNode(self, x, y):
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
            self.length[y] += self.length[x]
        else:
            self.parents[y] = x
            self.length[x] += self.length[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #ノードxが含まれるグループの要素数を返す関数
    def getLength(self, x):
        x = self.findRoot(x)
        return self.length[x]        

    #ノードxとノードyが同じグループであるかを返す関数
    def isSameGroup(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

    #グループの数を返す関数
    def getNumberOfGroup(self):
        s = set()
        for i in range(self.numberOfElements):
            s.add(self.findRoot(i))
        return len(s)

def main():
    n, m = map(int, readline().split())
    uf = UnionFind(n)
    for _ in range(m):
        x, y, z = map(int, readline().split())
        uf.uniteNode(x-1, y-1)
    print(uf.getNumberOfGroup())
if __name__ == '__main__':
    main()
